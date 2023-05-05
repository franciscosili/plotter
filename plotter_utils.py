import ROOT as RT
import ctypes
from seaborn import color_palette
from typing  import Union, Literal
from histutils import histogram_equal_to, histogram_normalize, get_ratio_hist, get_first_hist_dict

formats = ['pdf', 'eps']

#===================================================================================================
colourdict = {
    'black':       '#000000',
    'blue':        '#348ABD',
    'red':         '#A60628',
    'orange':      '#E24A33',
    'purple':      '#7A68A6',
    'lblue':       '#68add5',
    'turquoise':   '#188487',
    'pink':        '#CF4457',
    'green':       '#32b43c',
    'yellow':      '#e2a233',
    'grey':        '#838283',
    'lgreen':      '#88de8f',
    'lyellow':     '#f7fab3',
}
#===================================================================================================

#===================================================================================================
def get_color(c):
    """Get ROOT color from name or HEX code

    Args:
        c (str): Name of the color, or HEX code, or ROOT color code

    Returns:
        TColor: ROOT colour
    """
    if not isinstance(c, str):
        return c

    if c.startswith('#'):
        colour = RT.TColor.GetColor(c)
    else:
        try:
            colour = RT.TColor.GetColor(colourdict[c])
        except KeyError:
            if '+' in c:
                col, n = c.split('+')
                colour = getattr(RT, col)
                colour += int(n)
            elif '-' in c:
                col, n = c.split('-')
                colour = getattr(RT, col)
                colour -= int(n)
            else:
                colour = getattr(RT, c)

    return colour
#===================================================================================================

#===================================================================================================
def set_color(obj, color, fill=False, alpha=None):
    """Set color to object

    Args:
        obj (*): Object to apply color
        color (str): Name of color
        fill (bool, optional): whether to set the filling color or not. Defaults to False.
        alpha (float, optional): transparency value for filling. Defaults to None.
    """
    color = get_color(color)
    obj.SetLineColor(color)
    obj.SetMarkerColor(color)
    if fill:
        if alpha is not None:
            obj.SetFillColorAlpha(color, alpha)
        else:
            obj.SetFillColor(color)
    return
#===================================================================================================

#===================================================================================================
def get_colors_seaborn(number_colors, iel):
    colors = color_palette('muted', number_colors)
    return colors.as_hex()[iel]
#===================================================================================================

#===================================================================================================
def set_style(obj, **kwargs):
    """Set style attributes to object

    Args:
        obj (*): object to which the style attributes are applied
    """

    # check if hist or graph 
    is_hist = obj.InheritsFrom('TH1')

    color = kwargs.get('color', RT.kBlack)
    alpha = kwargs.get('alpha', None)

    mstyle = kwargs.get('mstyle', 20)   # marker style
    fstyle = kwargs.get('fstyle', None) # fill style
    lstyle = kwargs.get('lstyle',None)  # line style

    msize  = kwargs.get('msize', 0.8)  # marker size
    lwidth = kwargs.get('lwidth', 2)   # line width

    fill = (kwargs.get('fill', False) or fstyle is not None)

    xtitle = kwargs.get('xtitle', None)
    ytitle = kwargs.get('ytitle', None)

    xmin = kwargs.get('xmin', None)
    xmax = kwargs.get('xmax', None)
    ymin = kwargs.get('ymin', None)
    ymax = kwargs.get('ymax', None)

    # default
    obj.SetTitle('')
    if is_hist:
        obj.SetStats(0)

    # color
    set_color(obj, color, fill, alpha)

    # marker
    obj.SetMarkerStyle(mstyle)
    obj.SetMarkerSize(msize)

    # line
    obj.SetLineWidth(lwidth)
    if lstyle is not None:
        obj.SetLineStyle(lstyle)

    # fill
    if fstyle is not None:
        obj.SetFillStyle(fstyle)

    # axis titles
    if xtitle is not None:
        obj.GetXaxis().SetTitle(xtitle)
    if ytitle is not None:
        obj.GetYaxis().SetTitle(ytitle)

    if xmin is not None and xmax is not None:
        obj.GetXaxis().SetRangeUser(xmin, xmax)
    if ymin is not None and ymax is not None:
        obj.GetYaxis().SetRangeUser(ymin, ymax)
    return
#===================================================================================================

#===================================================================================================
def binwidth_formatting(width: float) -> Literal['{:.0f}', '{:.2f}']:
    if width > 10:
        format_str = '{:.0f}'
    else:
        format_str = '{:.2f}'
    return format_str
#===================================================================================================

#===================================================================================================
def latex_label(x      : float,
                y      : float,
                color  : int,
                text   : str,
                size   : float = None,
                do_draw: bool = True) -> RT.TLatex:
    lat = RT.TLatex()
    lat.SetTextFont(42)
    lat.SetTextColor(color)
    if size:
        lat.SetTextSize(size)
    if do_draw:
        return lat.DrawLatexNDC(x, y, text)
    else:
        lat.SetText(x, y, text)
        return lat
#===================================================================================================

#===================================================================================================
def get_pad_size(pad: RT.TPad) -> float:
    return get_pad_height(pad)*get_pad_width(pad)
#===================================================================================================

#===================================================================================================
def get_pad_height(pad: RT.TPad) -> float:
    return pad.GetHNDC()*pad.GetWh()
#===================================================================================================

#===================================================================================================
def get_pad_width(pad: RT.TPad) -> float:
    return pad.GetWNDC()*pad.GetWw()
#===================================================================================================

#===================================================================================================
def optimal_textsize_legend(textsize, labels, xmin, xmax, ncols, pad_resolution=1.) -> float:
    # initial labels width
    curr_width = max([latex_label(xmin, 0.4, 1, l, do_draw=False).GetXsize() for l in labels])*pad_resolution

    curr_textsize      = textsize
    max_possible_width = xmax-xmin-0.05
    
    if curr_width*ncols > max_possible_width:
        # need to decrease size
        while curr_width*ncols > max_possible_width:
            curr_textsize -= 0.01 * pad_resolution
            curr_width     = max([latex_label(xmin, 0.4, 1, l, curr_textsize, False).GetXsize() for l in labels])
    else:
        # can increase size
        while (curr_width*ncols < max_possible_width) and (curr_width*ncols < textsize):
            curr_textsize += 0.01 * pad_resolution
            curr_width     = max([latex_label(xmin, 0.4, 1, l, curr_textsize, False).GetXsize() for l in labels])
        
        # we went too far
        if curr_width*ncols > max_possible_width:
            curr_textsize -= 0.01 * pad_resolution

    return curr_textsize
#===================================================================================================

#===================================================================================================
def overlapped_yrange(chist, minimum_labels, plotted_objs, use_error=False) -> None:

    # check if we are using logscale
    logy = RT.gPad.GetLogy()





    # get the maximum of the plotted objects and its location
    plotted_maxs = []
    plotted_mins = []


    for obj in plotted_objs:
        min_val = float('inf')
        max_val = 0
        max_loc = -1
        min_loc = -1
        if obj.InheritsFrom('TH1'):
            for this_bin in range(1, obj.GetNbinsX()+1):
                tmp_max = obj.GetBinContent(this_bin)
                tmp_min = obj.GetBinContent(this_bin)
                tmp_err_up = obj.GetBinErrorUp(this_bin)
                tmp_err_dw = obj.GetBinErrorLow(this_bin)
                if use_error:
                    tmp_max += tmp_err_up
                    tmp_min -= tmp_err_dw
                if tmp_max > max_val:
                    max_val = tmp_max
                    max_loc = this_bin
                if tmp_min < min_val:
                    min_val = tmp_min
                    min_loc = this_bin
            
            plotted_maxs.append((max_val,
                                 obj.GetBinLowEdge(max_loc),
                                 obj.GetBinLowEdge(max_loc) + obj.GetBinWidth(max_loc)))
            plotted_mins.append((min_val,
                                 obj.GetBinLowEdge(min_loc),
                                 obj.GetBinLowEdge(min_loc) + obj.GetBinWidth(min_loc)))

        elif obj.InheritsFrom('TGraph'):
            num = obj.GetN()
            for this_point in range(0, num):
                tmp_max = obj.GetPointY(this_point) + obj.GetErrorYhigh(this_point)
                tmp_min = obj.GetPointY(this_point) - obj.GetErrorYlow(this_point)
                if tmp_max > max_val:
                    max_val = tmp_max
                    max_loc = this_point
                if tmp_min < min_val:
                    min_val = tmp_min
                    min_loc = this_point
                
            point_xmin = obj.GetPointX(max_loc) - obj.GetErrorXlow(max_loc)
            point_xmax = obj.GetPointX(max_loc) + obj.GetErrorXhigh(max_loc)
            plotted_maxs.append((point_xmin, point_xmax, max_val))
            plotted_mins.append((point_xmin, point_xmax, min_val))

    max_object_values = max(plotted_maxs, key= lambda x: x[0])[0]
    min_object_values = min(plotted_mins, key= lambda x: x[0])[0]

    chist.SetMaximum(max_object_values)

    if logy:
        chist.SetMinimum(0.01*min_object_values)
    else:
        chist.SetMinimum(0.6*min_object_values)

    def is_overlapped() -> bool:
        RT.gPad.Modified()
        RT.gPad.Update()
        min_labels_user = RT.gPad.PixeltoY(RT.gPad.VtoPixel(minimum_labels) - int(RT.gPad.GetWh()*RT.gPad.GetHNDC()))
        min_labels_user = 10**min_labels_user if logy else min_labels_user

        if max_object_values >= min_labels_user:
            return True
        return False
    

    counter = 0
    old_maximum = RT.gPad.GetUymax()
    while is_overlapped():
        new_maximum = RT.gPad.GetUymax()
        
        if logy:
            new_maximum = 10**(new_maximum + 0.3) # Since SetMaximum requieres an absolute scale...
        else:
            new_maximum *= 1.05
        
        chist.SetMaximum(new_maximum)
        RT.gPad.Modified()
        RT.gPad.Update()

        counter += 1
        if counter > 50:
            #Failover for crappy ROOT behaviour
            new_maximum = old_maximum
            if logy:
                new_maximum = 10**(new_maximum + 3) # Since SetMaximum requieres an absolute scale...
            else:
                new_maximum *= 1.3
            chist.SetMaximum(new_maximum)
            RT.gPad.Modified()
            RT.gPad.Update()
            
            break
    return
#===================================================================================================

#===================================================================================================
def draw_ratio_lines(ratio, yvals, xmin=None, xmax=None):

    if not xmin and not xmax:
        firstbin = ratio.GetXaxis().GetFirst()
        lastbin  = ratio.GetXaxis().GetLast()
        xmax     = ratio.GetXaxis().GetBinUpEdge(lastbin)
        xmin     = ratio.GetXaxis().GetBinLowEdge(firstbin)

    lines = [None]*len(yvals)
    for i, y in enumerate(yvals):
        lines[i] = RT.TLine(xmin, y, xmax, y)
        RT.SetOwnership(lines[i], False)

    lines[0].SetLineWidth(1)
    lines[0].SetLineStyle(2)
    for line in lines[1:]:
        line.SetLineStyle(3)

    for line in lines:
        line.AppendPad()
        line.Draw()
    return
#===================================================================================================

#===================================================================================================
def get_axis_tick_positions(hist, ax='y', level='major'):

    if ax == 'y':
        lim_min = hist.GetMinimum()
        lim_max = hist.GetMaximum()
        # get axis ndivisions and get major 
        ndiv    = hist.GetYaxis().GetNdivisions()
    elif ax == 'x':
        lim_min = hist.GetXaxis().GetXmin()
        lim_max = hist.GetXaxis().GetXmax()
        # get axis ndivisions and get major 
        ndiv    = hist.GetXaxis().GetNdivisions()

    if level == 'major':
        ndiv = ndiv %  100
    elif level == 'minor':
        ndiv = ndiv // 100

    nbins_optimized    = ctypes.c_int(0)
    lim_min_optimized  = ctypes.c_double(0.)
    lim_max_optimized  = ctypes.c_double(0.)
    binwidth_optimized = ctypes.c_double(0.)

    RT.THLimitsFinder.Optimize(lim_min, lim_max, ndiv, lim_min_optimized, lim_max_optimized,
                               nbins_optimized, binwidth_optimized, "")
    
    lim_min_optimized  = lim_min_optimized.value
    lim_max_optimized  = lim_max_optimized.value
    binwidth_optimized = binwidth_optimized.value
    nbins_optimized    = nbins_optimized.value
    
    # first y-label
    ylabel = lim_min_optimized
    
    tick_pos = []

    for i in range(nbins_optimized+1):
        tick_pos.append(ylabel)
        ylabel = ylabel + binwidth_optimized

    return tick_pos
#===================================================================================================
