import ROOT as RT
from ATLASstyle import ATLASlabel
from style import get_plotconf
from typing import Union, Literal
from seaborn import color_palette


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
def binwidth_formatting(width: float) -> Literal['{:.0f}', '{:.2f}']:
    if width > 10:
        format_str = '{:.0f}'
    else:
        format_str = '{:.2f}'
    return format_str
#===================================================================================================

#===================================================================================================
def overlapped_yrange(chist, minimum_labels, plotted_objs, use_error=False) -> None:

    # check if we are using logscale
    logy = RT.gPad.GetLogy()

    # get the maximum of the plotted objects and its location
    plotted_maxs = []


    for obj in plotted_objs:
        max_val = 0
        max_loc = -1
        if obj.InheritsFrom('TH1'):
            for this_bin in range(1, obj.GetNbinsX()+1):
                tmp_max = obj.GetBinContent(this_bin)
                tmp_err = obj.GetBinErrorUp(this_bin)
                if use_error:
                    tmp_max += tmp_err
                if tmp_max > max_val:
                    max_val    = tmp_max
                    max_loc = this_bin
            
            plotted_maxs.append((max_val,
                                 obj.GetBinLowEdge(max_loc),
                                 obj.GetBinLowEdge(max_loc) + obj.GetBinWidth(max_loc)))

        elif obj.InheritsFrom('TGraph'):
            num = obj.GetN()
            for this_point in range(0, num):
                tmp_max = obj.GetPointY(this_point) + obj.GetErrorYhigh(this_point)
                if tmp_max > max_val:
                    max_val = tmp_max
                    max_loc = this_point
                
            point_xmin = obj.GetPointX(max_loc) - obj.GetErrorXlow(max_loc)
            point_xmax = obj.GetPointX(max_loc) + obj.GetErrorXhigh(max_loc)
            plotted_maxs.append((point_xmin, point_xmax, max_val))

    max_object_values = max(plotted_maxs, key= lambda x: x[0])[0]

    chist.SetMaximum(max_object_values)

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
class plotter:
    plottypes = ('cmp',             # comparison between histograms. Can have ratio
                 'data_signal_bkg', # Data vs Signal vs backgrond comparison
                 'values',          # plot simple values
                 'values_graph',    # plot simple values coming from TGraphs
                 'fit',             # fits
                 'roofit',          # roofit results
                 'stack'            # a simple stack
                )
    dw_pad_types = ('ratio',       # Simple ratio between histograms/values/functions in the upper pad
                    'signal_bkg',  # Signal / backgrond
                    'SB',          # SB significance
                    'effrej',      # Efficiency-rejection
                    'significance',# significance
                    'default',     # data / SM
                    'values',      # another set of values
                )
    #===============================================================================================
    def __init__(self,
                 pads2      : bool,
                 plottype   : str,
                 xvar       : str,
                 chist,
                 **kwargs) -> None:

        RT.gROOT.SetStyle('ATLAS')

        self.width       = kwargs.get('width'        , 800)
        self.height      = kwargs.get('height'       , 800)
        pads_division    = kwargs.get('pads_division', 0.35)
        dw_pad_type      = kwargs.get('dw_pad_type'  , 'ratio')
        yvar_up          = kwargs.get('yvar_up'      , 'entries')
        yvar_dw          = kwargs.get('yvar_dw'      , 'ratio')
        chist_dw         = kwargs.get('chist_dw'     , None)
        self.atlas_label = kwargs.get('atlas_label'  , 'none')
        self.legcols     = kwargs.get('legcols'      , 1)
        self.year        = kwargs.get('year'         , 'Run2')
        self.cme         = kwargs.get('cme'          , 13)
        self.lumi        = kwargs.get('cme'          , 140)
        
        # ------------------------------------------------------------------
        # General properties
        # ------------------------------------------------------------------
        if plottype not in (self.plottypes):
            raise ValueError(f'Error: plot_type not set properly. Choose one of the following {self.plottypes}')
        self.plot_type = plottype

        # whether we have different x/y variables
        self.separated_xy_variables = self.plot_type not in ('cmp', 'data_signal_bkg', 'fit', 'roofit', 'stack')

        if dw_pad_type not in (self.dw_pad_types):
            raise ValueError(f'Error: dw_pad_type not set properly. Choose one of the following {self.dw_pad_types}')
        self.dw_pad_type = dw_pad_type
        
        self.xvar      = xvar
        self.yvar_up   = yvar_up
        self.yvar_dw   = yvar_dw

        # ------------------------------------------------------------------
        # Drawable objects
        # ------------------------------------------------------------------
        self.data        = []
        self.signals     = []
        self.bkg         = []
        self.hists       = []
        self.graphs      = []
        self.labels      = []
        self.dwpad_hists = []
        self.chist_up    = chist
        self.chist_dw    = chist_dw

        # ------------------------------------------------------------------
        # Canvas and pads creation
        # ------------------------------------------------------------------
        self.can     = RT.TCanvas('', '', self.width, self.height)
        self.pads2   = pads2

        self.canvas_size = self.width*self.height

        # auxiliary pad to compute resolutions. This is never drawn
        aux_pad = RT.TPad('', '', 0, 0, 1, 1, 0, 0, 0)
        self.resolution_single_pad = self.canvas_size/get_pad_size(aux_pad)
        del aux_pad
        
        print(f'{self.resolution_single_pad = }')
        
        
        if not self.pads2:
            self.uppad = RT.TPad('up', 'up', 0, 0, 1, 1, 0, 0, 0)
            self.dwpad = None
            
            self.resolution_uppad   = self.canvas_size / get_pad_size(self.uppad)
            self.resolution_y_uppad = self.height / get_pad_height(self.uppad)
            self.resolution_x_uppad = self.width  / get_pad_width(self.uppad)

        else:
            # we have two pads
            # up pad
            self.uppad = RT.TPad('up', 'up', 0, pads_division, 1, 1, 0, 0, 0)
            
            self.resolution_uppad   = self.canvas_size / get_pad_size(self.uppad)
            self.resolution_y_uppad = self.height / get_pad_height(self.uppad)
            self.resolution_x_uppad = self.width  / get_pad_width(self.uppad)
            
            print(f'{self.resolution_x_uppad = },    {self.resolution_y_uppad = },    {self.resolution_uppad = }')

            # down pad
            self.dwpad = RT.TPad('dw', 'dw', 0, 0, 1, pads_division, 0, 0, 0)
            
            self.resolution_dwpad    = self.canvas_size / get_pad_size(self.dwpad)
            self.resolution_y_dwpad  = self.height / get_pad_height(self.dwpad)
            self.resolution_x_dwpad  = self.width  / get_pad_width(self.dwpad)
            
            print(f'{self.resolution_x_dwpad = },    {self.resolution_y_dwpad = },    {self.resolution_dwpad = }')

        
        # ------------------------------------------------------------------
        # Dimensions definitions
        # ------------------------------------------------------------------
        bottom_margin      = 0.10
        left_margin        = 0.10
        right_margin       = 0.05
        self.text_size     = 0.04
        self.text_height   = 0.044
        self.tick_length   = 0.02
        self.offset        = 1.30

        # ------------------------------------------------------------------
        # Upper pad modification
        # ------------------------------------------------------------------
        # margins
        self.uppad.SetTopMargin(0.05*self.resolution_y_uppad)
        if self.pads2:
            self.uppad.SetBottomMargin(0.006*self.resolution_y_uppad)
        else:
            self.uppad.SetBottomMargin(bottom_margin)
        self.uppad.SetLeftMargin (left_margin *self.resolution_x_uppad)
        self.uppad.SetRightMargin(right_margin*self.resolution_x_uppad)
        # others
        self.uppad.SetTicks(1,1)
        self.uppad.SetFrameBorderMode(0)
        self.uppad.SetFillStyle(0)

        self.uppad.Draw()
        
        # ------------------------------------------------------------------
        # Lower pad modification
        # ------------------------------------------------------------------
        if self.pads2:
            # margins
            self.dwpad.SetTopMargin(0.0)
            self.dwpad.SetBottomMargin(bottom_margin*self.resolution_y_dwpad)
            self.dwpad.SetLeftMargin  (left_margin  *self.resolution_x_dwpad)
            self.dwpad.SetRightMargin (right_margin *self.resolution_x_dwpad)
            # others
            self.dwpad.SetTicks(1,1)
            self.dwpad.SetFrameBorderMode(0)
            self.dwpad.SetFillStyle(0)

            self.dwpad.Draw()

    
        # ------------------------------------------------------------------
        # Labels positioning
        # ------------------------------------------------------------------
        self.labels_positions = {}

        self.uppad.cd()
        return
    #===============================================================================================
    
    #===============================================================================================
    #   FORMATTING
    #===============================================================================================
    #===============================================================================================
    def format_up(self, conf_x, conf_y=None) -> None:

        # values definitions
        resolution_scale       = (self.resolution_uppad/self.resolution_single_pad)
        self.text_size_uppad   = self.text_size   * resolution_scale
        self.text_height_uppad = self.text_height * resolution_scale
    

        # ticks
        tick_length = self.tick_length * resolution_scale
        self.chist_up.GetYaxis().SetTickLength(tick_length)
        self.chist_up.GetXaxis().SetTickLength(tick_length)


        # log scale in vertical axis
        if not self.separated_xy_variables:
            if conf_x.logy:
                self.uppad.SetLogy()
        else:
            if conf_y.logx:
                self.uppad.SetLogy()
        
        # log scale in horizontal axis
        if conf_x.logx:
            self.uppad.SetLogx()

        
        # axis labelling and style
        self.chist_up.GetYaxis().SetLabelSize(self.text_size_uppad)
        self.chist_up.GetYaxis().SetTitleSize(self.text_size_uppad)
        self.chist_up.GetXaxis().SetLabelSize(self.text_size_uppad)
        self.chist_up.GetXaxis().SetTitleSize(self.text_size_uppad)


        binw       = self.chist_up.GetXaxis().GetBinWidth(1)
        format_str = binwidth_formatting(binw)
        
        self.chist_up.GetXaxis().SetTitle(conf_x.xtitle)
        if not self.separated_xy_variables:
            # we get the y title from the xtitle of conf_y
            self.chist_up.GetYaxis().SetTitle(conf_x.ytitle.replace('BIN', format_str.format(binw)))
        else:
            self.chist_up.GetYaxis().SetTitle(conf_y.xtitle.replace('BIN', format_str.format(binw)))
        

        # y title offset
        offset = self.offset * get_pad_height(self.uppad) / get_pad_width(self.uppad)
        self.chist_up.GetYaxis().SetTitleOffset(offset)


        self.labels_positions['up'] = {
            'l': self.uppad.GetLeftMargin()  + self.resolution_x_uppad*0.04,
            'r': 0.25*(3 + self.uppad.GetLeftMargin() - 3.*self.uppad.GetRightMargin()),
            't': 1 - 2.*self.text_height_uppad - 0.015,
            'b': self.uppad.GetBottomMargin() + self.text_height_uppad,
        }

        return
    #===============================================================================================
    
    #===============================================================================================
    def format_dw(self, ytitle, yrange) -> None:

        resolution_scale      = (self.resolution_dwpad/self.resolution_single_pad)
        self.text_size_dwpad   = self.text_size * resolution_scale
        self.text_height_dwpad = self.text_height * resolution_scale

        
        # ticks
        tick_length = self.tick_length * resolution_scale
        self.chist_dw.GetYaxis().SetTickLength(tick_length)
        self.chist_dw.GetXaxis().SetTickLength(tick_length)

        # log scale in horizontal axis
        if self.uppad.GetLogx():
            self.dwpad.SetLogx()
            self.chist_dw.SetMoreLogLabels()


        # axis labelling and style
        self.chist_dw.GetYaxis().SetLabelSize(self.text_size_dwpad)
        self.chist_dw.GetYaxis().SetTitleSize(self.text_size_dwpad)
        self.chist_dw.GetXaxis().SetLabelSize(self.text_size_dwpad)
        self.chist_dw.GetXaxis().SetTitleSize(self.text_size_dwpad)
        

        self.chist_dw.GetYaxis().SetTitle(ytitle)
        # set x title the same as the top pad
        self.chist_dw.GetXaxis().SetTitle(self.chist_up.GetXaxis().GetTitle())
        
        # remove labels and x bin labels from top pad
        self.chist_up.GetXaxis().SetTitle("")
        self.chist_up.GetXaxis().SetLabelSize(0)


        # y title offset
        offset = self.offset * get_pad_height(self.dwpad) / get_pad_width(self.dwpad)
        self.chist_dw.GetYaxis().SetTitleOffset(offset)
        self.chist_dw.GetYaxis().CenterTitle()
        
        if self.dw_pad_type == 'ratio':
            self.chist_dw.GetYaxis().SetNdivisions(403)
        else:
            self.chist_dw.GetYaxis().SetNdivisions(503)


        # y range
        self.chist_dw.SetMinimum(yrange[0])
        self.chist_dw.SetMaximum(yrange[1])


        self.labels_positions['dw'] = {
            'l': self.dwpad.GetLeftMargin()  + self.resolution_x_dwpad*0.04,
            'r': 0.25*(3 + self.dwpad.GetLeftMargin() - 3.*self.dwpad.GetRightMargin()),
            't': 1 - self.text_height_dwpad - 0.015,
            'b': self.dwpad.GetBottomMargin() + 0.8*self.text_height_dwpad,
        }

        return
    #===============================================================================================



    #===============================================================================================
    #   PLOTTING
    #===============================================================================================
    #===============================================================================================
    def plot(self, plotname, plot_format=formats) -> None:

        # ------------------------------------------------------------------
        # Upper pad
        # ------------------------------------------------------------------
        # draw first and empty histogram
        self.chist_up.Draw()

        # draw plot labels
        max_labelx, minmax_labely = self.plot_labels(self.uppad, self.text_size_uppad,
                                                          self.text_height_uppad,
                                                          self.atlas_label)
        # draw legend
        leg = self.plot_legend(self.uppad, max_labelx, ncols=self.legcols)
        leg.Draw()

        # draw hists
        plotted_objs = self.plot_hists()

        # update range to accomodate all labels and distributions
        overlapped_yrange(self.chist_up, min(minmax_labely['ymin'], leg.GetY1()), plotted_objs)

        # update upper pad to accomodate range
        self.uppad.Update()

        # ------------------------------------------------------------------
        # Lower pad
        # ------------------------------------------------------------------
        if self.pads2:
            self.dwpad.cd()
            self.chist_dw.Draw()

            max_labelx, minmax_labely = self.plot_labels(self.dwpad, self.text_size_dwpad,
                                                         self.text_height_dwpad)
            self.extra_ratio_plotting()
            self.plot_hists()
        
            

        # ------------------------------------------------------------------
        # Saving
        # ------------------------------------------------------------------
        self.can.cd()

        if not isinstance(plot_format, list): plot_format = [plot_format, ]
        for this_format in plot_format:
            self.can.SaveAs(f'{plotname}.{this_format}')

        return
    #===============================================================================================

    #===============================================================================================
    def plot_labels(self,
                    pad        : RT.TPad,
                    size       : int | float,
                    text_height: int | float,
                    atlas_label: str ='none') -> tuple[float, dict[str, float]]:
        
        # make sure to plot in the desired pad
        pad.cd()
        # check if we have the uppad or dwpad
        padpos = pad.GetName()
        uppad  = (padpos == 'up')

        # to know the size of the biggest label
        labels = []

        # this dictionary saves the next-to-use value of x/y for each position and canvas
        yrange_extremes = {'ymin' : -1, 'ymax' : -1}

        # this dictionary saves the next-to-use value of x/y for each position and canvas
        possible_positions = ['tl', 'tr', 'bl', 'br']
        xy_plotted_vals    = { pos: [0, 0] for pos in possible_positions}

        # only plot atlas label and cme/lumi if we are in the uppad
        if uppad:
            xy_plotted_vals['tl'] = [self.labels_positions['up']['l'], self.labels_positions['up']['t']]
            
            if atlas_label != 'none':
                labels.append(ATLASlabel(*xy_plotted_vals['tl'],
                                         atlas_label, fontSize=size)
                             )
                xy_plotted_vals['tl'][1] -= text_height
                
            # cme and lumi label    
            if self.lumi is not None and self.cme is not None:
                labels.append(latex_label(*xy_plotted_vals['tl'], 1,
                                          f'#sqrt{{s}} = {self.cme} TeV, {self.lumi} fb^{{-1}}',
                                          size=size)
                             )
                xy_plotted_vals['tl'][1] -= text_height
            
        # labels
        # if not isinstance(labels, list): labels = [labels, ]
        if padpos not in self.labels or len(self.labels[padpos]) == 0:
            return None, None

        for this_label, label_pos in self.labels[padpos]:
            
            # get the x-y values from the dictionaries.
            ypos = ''
            xpos = ''
            for this_pos in label_pos:
                match this_pos:
                    case 'l':
                        xmin = self.labels_positions[padpos][this_pos]
                        xpos = this_pos
                    case 'r':
                        xmin = self.labels_positions[padpos][this_pos]
                        xpos = this_pos
                    case 't':
                        ymin = self.labels_positions[padpos][this_pos]
                        ypos = this_pos
                    case 'b':
                        ymin = self.labels_positions[padpos][this_pos]
                        ypos = this_pos

            
            if xy_plotted_vals[ypos+xpos][0] == 0:
                xy_plotted_vals[ypos+xpos][0] = xmin

            if xy_plotted_vals[ypos+xpos][1] == 0:
                xy_plotted_vals[ypos+xpos][1] = ymin
            
            labels.append(latex_label(*xy_plotted_vals[ypos+xpos],
                                      1, this_label, size=size))
            if ypos == 'b':
                xy_plotted_vals[ypos+xpos][1] += text_height
            elif ypos == 't':
                xy_plotted_vals[ypos+xpos][1] -= text_height
            

        yrange_extremes['ymin'] = min(v for v in [xy_plotted_vals['tl'][1], xy_plotted_vals['tr'][1]] if v > 0)
        yrange_extremes['ymax'] = max(xy_plotted_vals['bl'][1], xy_plotted_vals['br'][1])
        

        max_labelx = max([this_label.GetXsize() for this_label in labels]) + self.labels_positions['up']['l']
        return max_labelx, yrange_extremes
    #===============================================================================================
    
    #===============================================================================================
    def plot_legend(self, pad, x, vpos='t', ncols=1) -> None:
        # if its the upper or lower pad
        padpos = pad.GetName()
        
        resolution   = self.resolution_uppad   if padpos == 'up' else self.resolution_dwpad
        x_resolution = self.resolution_x_uppad if padpos == 'up' else self.resolution_x_dwpad
        y_resolution = self.resolution_y_uppad if padpos == 'up' else self.resolution_y_dwpad
        text_height  = self.text_height_uppad  if padpos == 'up' else self.text_height_dwpad
        text_size    = self.text_size_uppad    if padpos == 'up' else self.text_size_dwpad

        leg_x1   = x + 0.02*x_resolution
        leg_x2   = 1 - pad.GetRightMargin()
        
        # leg_x2   = 1 - 0.1*(self.width*1.0/self.uppad.GetWw())
        # leg_xmid = leg_x1 + 0.5*(leg_x2-leg_x1)
        leg_y    = self.labels_positions[padpos][vpos] + 0.5*text_height
        
        # determine the optimal text size for the legend
        labels = []
        if self.hists:
            nrows = len(self.hists)/ncols
            for _, label, _, _ in self.hists:
                labels.append(label)
        leg_textsize = optimal_textsize_legend(text_size, labels, leg_x1, leg_x2, ncols, resolution)
        
        # if(hasData) Nrows ++;
        # Nrows ++; // for "Uncertainty"
        # double legHeight = ((Nrows+fLegendNColumns-1)/fLegendNColumns)*textHeight;

        
        leg_height = ((nrows+ncols-1)/ncols)*text_height
        leg = RT.TLegend(leg_x1, leg_y-leg_height, leg_x2, leg_y, '', 'NDC')
        leg.SetNColumns(ncols)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        
        leg.SetTextFont(RT.gStyle.GetTextFont())
        leg.SetTextSize(leg_textsize)
        # leg.SetMargin(ncols*((0.85*self.uppad.GetWh())/(1.*self.uppad.GetWw()))*self.text_height/(leg_x2-leg_x1))

        if self.hists:
            for h, label, _, leg_opt in self.hists:
                leg.AddEntry(h, label, leg_opt)
        
        return leg
    #===============================================================================================
    
    #===============================================================================================
    def plot_hists(self) -> list | None:

        if RT.gPad.GetName() == 'up':
        
            plotted_objs = []
            if self.hists:
                for h, _, draw_opt, _ in self.hists:
                    h.Draw(f'SAME {draw_opt}')
                    plotted_objs.append(h)
            return plotted_objs
        
        else:
            for h, _, draw_opt, _ in self.dwpad_hists:
                h.Draw(f'SAME {draw_opt}')

            return
    #===============================================================================================
    
    #===============================================================================================
    def extra_ratio_plotting(self) -> None:

        if self.dw_pad_type == 'ratio':
            # get get the number of mayor and minor divisions in the y-axis
            ndivisions = self.chist_dw.GetYaxis().GetNdivisions()
            yrange     = [self.chist_dw.GetYaxis().GetXmin(), self.chist_dw.GetYaxis().GetXmax()]

            # get primary and secondary axis divisions
            primdiv = ndivisions // 100
            secdiv  = ndivisions % 100
            primdiv_ticks    = round((yrange[1]-yrange[0])/primdiv)
            max_primdiv_tick = yrange[0]
            # while max_primdiv_tick < yrange[1]:
            #     max_primdiv_tick += 
            secdiv_ticks  = round((yrange[1]-yrange[0])/primdiv)

            increment   = (yrange[1]-yrange[1])/secdiv
            ratio_lines = [1.0, ] + [increment*i for i in range(primdiv*secdiv)]
            draw_ratio_lines(self.chist_dw, ratio_lines)

        return
    #===============================================================================================



    #===============================================================================================
    #   SETTING UP
    #===============================================================================================
    #===============================================================================================
    def add_single_hist(self,
                 hist_type: str,
                 hist     : Union[RT.TH1F, RT.TH1D, RT.TGraph, RT.TGraphErrors, RT.TGraphAsymmErrors],
                 label    : str = None,
                 draw_opt : str = None,
                 leg_opt  : str = None,
                ) -> None:
        
        match hist_type:
            case 'hist':
                self.hists.append((hist, label, draw_opt, leg_opt))
            case 'data':
                self.data.append((hist, label, draw_opt, leg_opt))
            case 'signal':
                self.signals.append((hist, label, draw_opt, leg_opt))
            case 'bkg':
                self.bkg.append((hist, label, draw_opt, leg_opt))
            case 'graph':
                self.graphs.append((hist, label, draw_opt, leg_opt))
            case 'ratio':
                self.dwpad_hists.append((hist, label, draw_opt, leg_opt))
        
        return
    #===============================================================================================
    
    #===============================================================================================
    def add_hists(self,
                  hist_type: str,
                  hists    : list[list[Union[RT.TH1F, RT.TH1D, RT.TGraph, RT.TGraphErrors, RT.TGraphAsymmErrors],
                                       str, str, str]]
                  ) -> None:
    
        for this_h, this_label, this_draw_opt, this_leg_opt in hists:
            self.add_single_hist(hist_type, this_h, this_label, this_draw_opt, this_leg_opt)
        return
    #===============================================================================================

    #===============================================================================================
    def style_hists(self, objs, normalize=False, **kwargs) -> None:
        skip_nhists_colors = kwargs.get('skip_colors', 0)
        if isinstance(objs, list):
            for i, (h, _, _, _) in enumerate(objs):
                set_style(h, color=get_colors_seaborn(len(objs)+skip_nhists_colors, i+skip_nhists_colors),
                          **kwargs)
                if normalize: histogram_normalize(h)
        else:
            set_style(objs, color=get_colors_seaborn(1, 0), **kwargs)
            if normalize: histogram_normalize(objs)
        return
    #===============================================================================================

    #===============================================================================================
    def set_labels(self, labels) -> None:
        self.labels = {'up': []}
        if self.pads2:
            self.labels['dw'] = []
                
        for this_label in labels:
            if this_label[1] in self.labels:
                self.labels[this_label[1]].append((this_label[0], this_label[2]))

        return
    #===============================================================================================
#===================================================================================================


#===================================================================================================
def plot_cmp(chist, chist_dw, plotname, xvar, hists, labels, ratio, year='Run2', rationame=None, extra_x=None, yvar=None, extra_y=None):

    ratios = []
    for ihist, (h, _, _, _) in enumerate(hists):
        if ihist!=0:
            ratios.append((get_ratio_hist(hists[0][0], h, h.GetName()+'__ratio'), '', 'e', ''))


    # variables configuraiton
    conf_x = get_plotconf(xvar)
    if extra_x: conf_x.update_conf(**extra_x)
    
    if yvar   : conf_y = get_plotconf(yvar)
    if extra_y: conf_y.update_conf(**extra_y)

    p = plotter  (ratio, 'cmp', xvar, chist, yvar_up=yvar, atlas_label='Internal', legcols=2, chist_dw=chist_dw, pads_division=0.5)
    p.format_up  (conf_x=conf_x)
    if ratio:
        p.format_dw  ('H1 / Hs', [0, 2.2])
    
    p.add_hists  ('hist' , hists)
    p.add_hists  ('ratio', ratios)
    p.style_hists(p.hists, lwidth=1, alpha=0.3, fill=True)
    p.style_hists(p.dwpad_hists, lwidth=1, msize=1.0, skip_colors=1)
    p.set_labels (labels)
    

    p.plot(plotname, 'pdf')
    

    return
#===================================================================================================










hist1 = RT.TH1F("hist1", "Example Histogram 1", 50, -5, 5)
hist2 = RT.TH1F("hist2", "Example Histogram 2", 50, -5, 5)
# hist3 = RT.TH1F("hist3", "Example Histogram 3", 50, -5, 5)
# hist4 = RT.TH1F("hist4", "Example Histogram 4", 50, -5, 5)
# hist5 = RT.TH1F("hist5", "Example Histogram 5", 50, -5, 5)
# hist6 = RT.TH1F("hist6", "Example Histogram 6", 50, -5, 5)

for i in range(100):
    hist1.Fill(RT.gRandom.Gaus(-1, 1))
    hist2.Fill(RT.gRandom.Gaus(0 , 1))
    # hist3.Fill(RT.gRandom.Gaus(0, 0.6))
    # hist4.Fill(RT.gRandom.Gaus(-1, 0.6))
    # hist5.Fill(RT.gRandom.Gaus(0, 1.3))
    # hist6.Fill(RT.gRandom.Gaus(0, 0.5))

hs = [
    (hist1, 'Histogram 1', 'hist', 'f'),
    (hist2, 'Histogram 2', 'hist', 'f'),
    # (hist3, 'Histogram 3', 'hist', 'f'),
    # (hist4, 'Histogram 4', 'hist', 'f'),
    # (hist5, 'Histogram 5', 'hist', 'f'),
    # (hist6, 'Histogram 6', 'hist', 'f'),
]

labels = [
    ('SR'        , 'up', 'tl'),
    ('un label'  , 'up', 'tl'),
    # ('otro label', 'up', 'br'),
    # ('otro label2', 'up', 'br'),
    # ('hola'       , 'dw', 'tl'),
    # ('hola'       , 'dw', 'tr'),
    # ('hola'       , 'dw', 'bl'),
]

# create the ratio plotter object
chist = histogram_equal_to(hs[0][0], 'chist')
chist_dw = histogram_equal_to(hs[0][0], 'chist_dw')
plot_cmp(chist, chist_dw, 'test', 'ph_eta', hs, labels, True)