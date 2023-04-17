import ROOT

# Legend labels
labels_dict = dict()
labels_dict['data']           = 'Data'
# ---- Main backgrounds
labels_dict['photonjet']      = '#gamma + jets'
labels_dict['photonjet_Pythia'] = '#gamma + jets Pythia'
labels_dict['ttgamma']        = 't#bar{t}#gamma' # /single-t \\gamma'
labels_dict['tth']            = 't#bar{t}H(#gamma#gamma/Z#gamma)'
labels_dict['zllgamma']       = 'Z(ll)#gamma'
labels_dict['znunugamma']     = 'Z(#nu#nu)#gamma'
labels_dict['wgamma']         = 'W#gamma'
labels_dict['vgammagamma']    = 'W#gamma#gamma/Z#gamma#gamma'
# ---- Fake backgrounds
labels_dict['diphoton']       = '#gamma#gamma'
labels_dict['multijet']       = 'Multijet'
labels_dict['wjets']          = 'W + jets'
labels_dict['zjets']          = 'Z + jets'
labels_dict['ttbar']          = 't#bar{t}'
labels_dict['vjets']          = 'W/Z + jets'
labels_dict['vgamma']         = 'W#gamma/Z#gamma'
labels_dict['zgamma']         = 'Z#gamma'
labels_dict['gammagamma']     = '#gamma#gamma/W#gamma#gamma/Z#gamma#gamma'
labels_dict['efake']          = 'e#rightarrow#gamma fake'
labels_dict['jfake']          = 'jet#rightarrow#gamma fake'
labels_dict['fakes']          = '#gamma fakes' ##'e#rightarrow#gamma/j#rightarrow#gamma'

labels_dict['smr']          = 'SMR'



# # labels for photon+jet resonances excited quarks
# from signalgrid import get_signal_name, qstar_grid, qbh_grid, get_props_from_signame, get_model_from_signame
# label_qstar = "m_{{{quark}^{{*}}}}={mass:.1f} GeV,  f={fval:.2f}"
# label_qbh   = "QBH n={ndim}, m_{{th}}={mass:.1f} GeV"

# for ndim, tuples in qbh_grid.items():
#     for tupl in tuples:
#         labels_dict[get_signal_name('QBH', dsid=tupl[0])] = label_qbh.format(ndim=ndim[1:], mass=tupl[1])
# for q, tuples in qstar_grid.items():
#     for tupl in tuples:
#         labels_dict[get_signal_name('qstar', dsid=tupl[0])] = label_qstar.format(quark=q, fval=tupl[1], mass=tupl[2])


# def get_label(sample):
#     try:
#         label = labels_dict[sample]
#     except KeyError:
#         props = get_props_from_signame(sample)
#         model = get_model_from_signame(sample)
#         if model == 'qstar':
#             label = label_qstar.format(**props)
#         else:
#             label = label_qbh.format(**props)
#     return label



# Colours
colors_dict = dict()
colors_dict['data']           = ROOT.kBlack
colors_dict['photonjet']      = '#9DA9C4' ##e03127'
colors_dict['photonjet_Pythia']= '#9DA9C4' ##e03127'
colors_dict['photonjet_nnlo'] = '#9DA9C4' ##e03127'
colors_dict['fakes']          = '#3b5998' ##1e42d0'
colors_dict['wgamma']         = '#fcdd5d' ##fcdd5d'
colors_dict['zgamma']         = '#9066b3'
colors_dict['ttgamma']        = '#21c133' #'#39dd4b'
colors_dict['tth']            = '#85c88c'
colors_dict['tthzgam']        = '#93e29c'
colors_dict['tthgamgam']      = '#639068'

colors_dict['efake']          = '#a4cee6'
colors_dict['jfake']          = '#348ABD'
colors_dict['multijet']       = '#348ABD'
colors_dict['diphoton']       = '#ffa04d'
colors_dict['zllgamma']       = '#f7fab4'
colors_dict['znunugamma']     = '#f7fab5'
colors_dict['vgamma']         = '#f8f59b'
colors_dict['wjets']          = '#BCBC93'
colors_dict['zjets']          = '#36BDBD'
colors_dict['vjets']          = '#a4cee6'
colors_dict['ttbar']          = '#7fad79'
colors_dict['vgammagamma']    = '#e5ac49'
colors_dict['vgammagamma224'] = '#b5ac49'
colors_dict['gammagamma']     = '#e5ac49'
colors_dict['others']         = '#676363'
colors_dict['smr']            = '#a5a3a3'

style_dict = {
    # qstar
    'qStar_f0p01_M500' : {'lstyle': 4, 'color': "#84366b"},
    'qStar_f0p01_M1000': {'lstyle': 4, 'color': "#5db54b"},
    'qStar_f0p01_M2000': {'lstyle': 4, 'color': "#c746c6"},
    'qStar_f0p10_M500' : {'lstyle': 7, 'color': "#84366b"},
    'qStar_f0p10_M1000': {'lstyle': 7, 'color': "#5db54b"},
    'qStar_f0p10_M2000': {'lstyle': 7, 'color': "#c746c6"},
    'qStar_f0p10_M3000': {'lstyle': 7, 'color': "#a6a940"},
    'qStar_f0p10_M4000': {'lstyle': 7, 'color': "#6447c4"},
    'qStar_f0p50_M500' : {'lstyle': 6, 'color': "#84366b"},
    'qStar_f0p50_M1000': {'lstyle': 6, 'color': "#5db54b"},
    'qStar_f0p50_M2000': {'lstyle': 6, 'color': "#c746c6"},
    'qStar_f0p50_M3000': {'lstyle': 6, 'color': "#a6a940"},
    'qStar_f0p50_M4000': {'lstyle': 6, 'color': "#6447c4"},
    'qStar_f0p50_M5000': {'lstyle': 6, 'color': "#d88c3d"},
    'qStar_f0p50_M6000': {'lstyle': 6, 'color': "#db4938"},
    'qStar_f0p75_M6000': {'lstyle': 3, 'color': "#db4938"},
    'qStar_f0p75_M7000': {'lstyle': 3, 'color': "#9b4138"},
    'qStar_f1p00_M500' : {'lstyle': 1, 'color': "#84366b"},
    'qStar_f1p00_M1000': {'lstyle': 1, 'color': "#5db54b"},
    'qStar_f1p00_M2000': {'lstyle': 1, 'color': "#c746c6"},
    'qStar_f1p00_M3000': {'lstyle': 1, 'color': "#a6a940"},
    'qStar_f1p00_M4000': {'lstyle': 1, 'color': "#6447c4"},
    'qStar_f1p00_M5000': {'lstyle': 1, 'color': "#d88c3d"},
    'qStar_f1p00_M5500': {'lstyle': 1, 'color': "#3f2f6a"},
    'qStar_f1p00_M6000': {'lstyle': 1, 'color': "#db4938"},
    'qStar_f1p00_M6500': {'lstyle': 1, 'color': "#7396cd"},
    'qStar_f1p00_M7000': {'lstyle': 1, 'color': "#9b4138"},
    # cstar
    'cStar_f0p01_M500' : {'lstyle': 9, 'color': "#84366b"},
    'cStar_f0p01_M1000': {'lstyle': 9, 'color': "#5db54b"},
    'cStar_f0p10_M500' : {'lstyle': 8, 'color': "#84366b"},
    'cStar_f0p10_M1000': {'lstyle': 8, 'color': "#5db54b"},
    'cStar_f0p10_M2000': {'lstyle': 8, 'color': "#c746c6"},
    'cStar_f0p50_M500' : {'lstyle': 5, 'color': "#84366b"},
    'cStar_f0p50_M1000': {'lstyle': 5, 'color': "#5db54b"},
    'cStar_f0p50_M2000': {'lstyle': 5, 'color': "#c746c6"},
    'cStar_f0p50_M3000': {'lstyle': 5, 'color': "#a6a940"},
    'cStar_f1p00_M500' : {'lstyle': 2, 'color': "#84366b"},
    'cStar_f1p00_M1000': {'lstyle': 2, 'color': "#5db54b"},
    'cStar_f1p00_M2000': {'lstyle': 2, 'color': "#c746c6"},
    'cStar_f1p00_M3000': {'lstyle': 2, 'color': "#a6a940"},
    'cStar_f1p00_M4000': {'lstyle': 2, 'color': "#6447c4"},
    # bstar
    'bStar_f0p01_M500' : {'lstyle': 9, 'color': "#84366b"},
    'bStar_f0p01_M1000': {'lstyle': 9, 'color': "#5db54b"},
    'bStar_f0p10_M500' : {'lstyle': 8, 'color': "#84366b"},
    'bStar_f0p10_M1000': {'lstyle': 8, 'color': "#5db54b"},
    'bStar_f0p10_M2000': {'lstyle': 8, 'color': "#c746c6"},
    'bStar_f0p50_M500' : {'lstyle': 5, 'color': "#84366b"},
    'bStar_f0p50_M1000': {'lstyle': 5, 'color': "#5db54b"},
    'bStar_f0p50_M2000': {'lstyle': 5, 'color': "#c746c6"},
    'bStar_f0p50_M3000': {'lstyle': 5, 'color': "#a6a940"},
    'bStar_f1p00_M500' : {'lstyle': 2, 'color': "#84366b"},
    'bStar_f1p00_M1000': {'lstyle': 2, 'color': "#5db54b"},
    'bStar_f1p00_M2000': {'lstyle': 2, 'color': "#c746c6"},
    'bStar_f1p00_M3000': {'lstyle': 2, 'color': "#a6a940"},
    'bStar_f1p00_M4000': {'lstyle': 2, 'color': "#6447c4"},
    
    # qbh n=1
    'QBH_n1_Mth1000': {'lstyle': 1, 'color': "#6fb09b"},
    'QBH_n1_Mth2000': {'lstyle': 1, 'color': "#d94a81"},
    'QBH_n1_Mth3000': {'lstyle': 1, 'color': "#416231"},
    'QBH_n1_Mth4000': {'lstyle': 1, 'color': "#be81cb"},
    'QBH_n1_Mth5000': {'lstyle': 1, 'color': "#947947"},
    'QBH_n1_Mth6000': {'lstyle': 1, 'color': "#4d626c"},
    'QBH_n1_Mth7000': {'lstyle': 1, 'color': "#000000"},
    # qbh n=6
    'QBH_n6_Mth3000': {'lstyle': 1, 'color': "#416231"},
    'QBH_n6_Mth4000': {'lstyle': 1, 'color': "#be81cb"},
    'QBH_n6_Mth5000': {'lstyle': 1, 'color': "#947947"},
    'QBH_n6_Mth6000': {'lstyle': 1, 'color': "#4d626c"},
    'QBH_n6_Mth7000': {'lstyle': 1, 'color': "#000000"},
    'QBH_n6_Mth8000': {'lstyle': 1, 'color': "#542f2c"},
    'QBH_n6_Mth9000': {'lstyle': 1, 'color': "#c79295"},
}

# Plot config
#===================================================================================================
class plot_conf:
    #===============================================================================================
    def __init__(self,
                 varname: str,
                 xtitle : str  ='',
                 ytitle : str  ='',
                 legpos : str  ='right',
                 logx   : bool =False,
                 logy   : bool =True,
                 xmin   : float=None,
                 xmax   : float=None,
                 ymin   : float=None,
                 ymax   : float=None,
                 ) -> None:
        self.var    = varname
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.legpos = legpos
        self.logx   = logx
        self.logy   = logy
        self.xmin   = xmin
        self.xmax   = xmax
        self.ymin   = ymin
        self.ymax   = ymax
        return
    #===============================================================================================
    
    #===============================================================================================
    def update_conf(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if hasattr(self, k) and getattr(self, k) != v:
                setattr(self, k, v)
        return
    #===============================================================================================
#===================================================================================================

plots_conf = {
    'default': plot_conf(
        varname = 'default',
        xtitle = '',
        ytitle = '',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True
    ),

    'cuts': plot_conf(
        varname = 'cuts',
        xtitle = '',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    # ------ PHOTONS
    'ph_n': plot_conf(
        varname = 'ph_n',
        xtitle = 'Number of photons',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'ph_pt': plot_conf(
        varname = 'ph_pt',
        xtitle = 'p_{T}^{#gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_pt[0]': plot_conf(
        varname = 'ph_pt[0]',
        xtitle = 'p_{T}^{leading-#gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'ph_pt[1]': plot_conf(
        varname = 'ph_pt[1]',
        xtitle = 'p_{T}^{subleading-#gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_iso': plot_conf(
        varname = 'ph_iso',
        xtitle = 'E_{T}^{cone20} - 0.022 #times  p_{T} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'ph_is_iso_ext': plot_conf(
        varname = 'ph_is_iso_ext',
        xtitle = 'Photon pass extended isolation',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_iso[0]': plot_conf(
        varname = 'ph_iso[0]',
        xtitle = 'Leading photon E_{T}^{iso} - 0.022 #times  p_{T} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_eta': plot_conf(
        varname = 'ph_eta',
        xtitle = '#eta^{#gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'abs(ph_eta[0])': plot_conf(
        varname = 'abs(ph_eta[0])',
        xtitle = '|#eta^{leading-#gamma}|',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'ph_eta[0]': plot_conf(
        varname = 'ph_eta[0]',
        xtitle = '#eta^{leading-#gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'ph_eta[1]': plot_conf(
        varname = 'ph_eta[1]',
        xtitle = '#eta^{subleading-#gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'ph_etas2': plot_conf(
        varname = 'ph_etas2',
        xtitle = '#eta^{#gamma}_{s2}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'ph_etas2[0]': plot_conf(
        varname = 'ph_etas2[0]',
        xtitle = '#eta_{s2}^{leading-#gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'ph_etas2[1]': plot_conf(
        varname = 'ph_etas2[1]',
        xtitle = '#eta_{s2}^{subleading-#gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'ph_phi': plot_conf(
        varname = 'ph_phi',
        xtitle = '#phi^{#gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_phi[0]': plot_conf(
        varname = 'ph_phi[0]',
        xtitle = '#phi^{leading-#gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'ph_phi[1]': plot_conf(
        varname = 'ph_phi[1]',
        xtitle = '#phi^{subleading-#gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_truth_pt': plot_conf(
        varname = 'ph_truth_pt',
        xtitle = 'p_{T}^{true #gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_etcone40': plot_conf(
        varname = 'ph_etcone40',
        xtitle = 'E_{T}^{cone40} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'ph_ptcone20': plot_conf(
        varname = 'ph_ptcone20',
        xtitle = 'p_{T}^{cone20} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_trackiso': plot_conf(
        varname = 'ph_trackiso',
        xtitle = 'p_{T}^{cone20} / p_{T}',
        ytitle = 'Events / BIN ',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ph_type': plot_conf(
        varname = 'ph_type',
        xtitle = 'Particle type',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'lph_n': plot_conf(
        varname = 'lph_n',
        xtitle = 'Number of loose photons',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'lph_pt': plot_conf(
        varname = 'lph_pt',
        xtitle = 'p_{T}^{loose #gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'lph_pt[0]': plot_conf(
        varname = 'lph_pt[0]',
        xtitle = 'p_{T}^{leading-loose #gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'lph_pt[1]': plot_conf(
        varname = 'lph_pt[1]',
        xtitle = 'p_{T}^{subleading-loose #gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'lph_iso': plot_conf(
        varname = 'lph_iso',
        xtitle = 'Loose photon E_{T}^{cone20} - 0.022 #times  p_{T} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'lph_iso[0]': plot_conf(
        varname = 'lph_iso[0]',
        xtitle = 'Leading loose photon E_{T}^{iso} - 0.022 #times  p_{T} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'lph_eta': plot_conf(
        varname = 'lph_eta',
        xtitle = '#eta^{loose #gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'lph_eta[0]': plot_conf(
        varname = 'lph_eta[0]',
        xtitle = '#eta^{leading-loose #gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'lph_eta[1]': plot_conf(
        varname = 'lph_eta[1]',
        xtitle = '#eta^{subleading-loose #gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'lph_etas2': plot_conf(
        varname = 'lph_etas2',
        xtitle = '#eta^{loose #gamma}_{s2}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'lph_etas2[0]': plot_conf(
        varname = 'lph_etas2[0]',
        xtitle = '#eta_{s2}^{leading-loose #gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'lph_etas2[1]': plot_conf(
        varname = 'lph_etas2[1]',
        xtitle = '#eta_{s2}^{subleading-loose #gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'lph_phi': plot_conf(
        varname = 'lph_phi',
        xtitle = '#phi^{loose #gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'lph_phi[0]': plot_conf(
        varname = 'lph_phi[0]',
        xtitle = '#phi^{leading-loose #gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'lph_phi[1]': plot_conf(
        varname = 'lph_phi[1]',
        xtitle = '#phi^{Subleading-loose #gamma}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'lph_truth_pt': plot_conf(
        varname = 'lph_truth_pt',
        xtitle = 'p_{T}^{true #gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'lph_etcone40': plot_conf(
        varname = 'lph_etcone40',
        xtitle = 'Loose photon E_{T}^{cone40} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'lph_etcone40[0]': plot_conf(
        varname = 'lph_etcone40[0]',
        xtitle = 'E_{T}^{cone40} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'lph_ptcone20': plot_conf(
        varname = 'lph_ptcone20',
        xtitle = 'Loose photon p_{T}^{cone20} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'lph_trackiso': plot_conf(
        varname = 'lph_trackiso',
        xtitle = 'Loose photon p_{T}^{cone20} / p_{T}',
        ytitle = 'Events / BIN ',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    # ------ JETS
    'jet_n': plot_conf(
        varname = 'jet_n',
        xtitle = 'Number of jets',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'bjet_n': plot_conf(
        varname = 'bjet_n',
        xtitle = 'Number of b-jets',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_pt': plot_conf(
        varname = 'jet_pt',
        xtitle = 'p^{jet}_{T} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_e': plot_conf(
        varname = 'jet_e',
        xtitle = 'E^{jet}_{T} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_eta': plot_conf(
        varname = 'jet_eta',
        xtitle = '#eta^{jet}',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'abs(jet_eta[0])': plot_conf(
        varname = 'abs(jet_eta[0])',
        xtitle = '|#eta^{leading jet}|',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'jet_phi': plot_conf(
        varname = 'jet_phi',
        xtitle = '#phi^{jet}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_isb': plot_conf(
        varname = 'jet_isb',
        xtitle = 'Is b-jet',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_pt[0]': plot_conf(
        varname = 'jet_pt[0]',
        xtitle = 'p_{T}^{leading jet} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_pt[1]': plot_conf(
        varname = 'jet_pt[1]',
        xtitle = 'p_{T}^{subleading jet} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_pt[2]': plot_conf(
        varname = 'jet_pt[2]',
        xtitle = 'p_{T}^{sub-subleading jet} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_eta[0]': plot_conf(
        varname = 'jet_eta[0]',
        xtitle = '#eta^{leading jet}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'jet_eta[1]': plot_conf(
        varname = 'jet_eta[1]',
        xtitle = '#eta^{subleading jet}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'jet_eta[2]': plot_conf(
        varname = 'jet_eta[2]',
        xtitle = '#eta^{sub-subleading jet}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'jet_phi[0]': plot_conf(
        varname = 'jet_phi[0]',
        xtitle = '#phi^{leading jet}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),    

    'jet_phi[1]': plot_conf(
        varname = 'jet_phi[1]',
        xtitle = '#phi^{subleading jet}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_phi[2]': plot_conf(
        varname = 'jet_phi[2]',
        xtitle = '#phi^{sub-subleading jet}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'jet_btag_pu': plot_conf(
        varname = 'jet_btag_pu',
        xtitle = 'DL1d tagging p_{u}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'jet_btag_pc': plot_conf(
        varname = 'jet_btag_pc',
        xtitle = 'DL1d tagging p_{c}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'jet_btag_pb': plot_conf(
        varname = 'jet_btag_pb',
        xtitle = 'DL1d tagging p_{b}',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'jet_btag_w': plot_conf(
        varname = 'jet_btag_w',
        xtitle = 'DL1d_{b-tag} score',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'dl1d_b': plot_conf(
        varname = 'dl1d_b',
        xtitle = 'DL1d_{b-tag} score',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'dl1d_c': plot_conf(
        varname = 'dl1d_c',
        xtitle = 'DL1d_{c-tag} score',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'jet_truthflavorid': plot_conf(
        varname = 'jet_truthflavorid',
        xtitle = 'Truth flavor ID',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'jetjet_m': plot_conf(
        varname = 'jetjet_m',
        xtitle = 'm_{jj}',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    

    # ------ PHOTON+JET
    'phjet_dphi': plot_conf(
        varname = 'phjet_dphi',
        xtitle = '#Delta#phi(#gamma, jet)',
        ytitle = 'Events / BIN',
        legpos = 'top',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'phjet_deta': plot_conf(
        varname = 'phjet_deta',
        xtitle = '#Delta#eta(#gamma, jet)',
        ytitle = 'Events / BIN',
        legpos = 'top',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'phjet_dr': plot_conf(
        varname = 'phjet_dr',
        xtitle = '#DeltaR(#gamma, jet)',
        ytitle = 'Events / BIN',
        legpos = 'top',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'phjet_dr_min': plot_conf(
        varname = 'phjet_dr_min',
        xtitle = '#DeltaR_{min}(#gamma, jet)',
        ytitle = 'Events / BIN',
        legpos = 'top',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'phjet_drmin': plot_conf(
        varname = 'phjet_drmin',
        xtitle = '#DeltaR_{min}(#gamma, jet)',
        ytitle = 'Events / BIN',
        legpos = 'top',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'phjet_m': plot_conf(
        varname = 'phjet_m',
        xtitle = 'm_{#gammaj} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'phjet_mq': plot_conf(
        varname = 'phjet_mq',
        xtitle = 'm_{q^{*}} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'phjet_mb': plot_conf(
        varname = 'phjet_mb',
        xtitle = 'm_{b^{*}} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'phjet_mc': plot_conf(
        varname = 'phjet_mc',
        xtitle = 'm_{c^{*}} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'phjet_mQBH': plot_conf(
        varname = 'phjet_mQBH',
        xtitle = 'm_{QBH} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'phjet_pt': plot_conf(
        varname = 'phjet_pt',
        xtitle = 'p_{T}^{#gammaj} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'phjet_eta': plot_conf(
        varname = 'phjet_eta',
        xtitle = '#eta_{#gammaj} [GeV]',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'phjet_phi': plot_conf(
        varname = 'phjet_phi',
        xtitle = '#phi_{#gammaj} [GeV]',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'phjet_pt/phjet_m': plot_conf(
        varname = 'phjet_pt/phjet_m',
        xtitle = 'p_{T}^{#gammaj}/m_{#gammaj}',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'ph_pt[0]/phjet_m': plot_conf(
        varname = 'ph_pt[0]/phjet_m',
        xtitle = 'p_{T}^{Leading #gamma}/m_{#gammaj}',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'ph_pt/phjet_m': plot_conf(
        varname = 'ph_pt/phjet_m',
        xtitle = 'p_{T}^{#gamma}/m_{#gammaj}',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'jet_pt_min/ph_pt': plot_conf(
        varname = 'jet_pt_min/ph_pt',
        xtitle = 'p_{T}^{closest jet} / p_{T}^{#gamma}',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),


    # ------ MET
    'met_et': plot_conf(
        varname = 'met_et',
        xtitle = 'E_{T}^{miss} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'met_phi': plot_conf(
        varname = 'met_phi',
        xtitle = '#phi^{miss} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'met_sig': plot_conf(
        varname = 'met_sig',
        xtitle = 'E_{T}^{miss} Significance [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'met_sumet': plot_conf(
        varname = 'met_sumet',
        xtitle = 'SumEt [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'met_ph_et': plot_conf(
        varname = 'met_ph_et',
        xtitle = 'E_{T}^{miss} Photon Term [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'met_jet_et': plot_conf(
        varname = 'met_jet_et',
        xtitle = 'E_{T}^{miss} Jet Term [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),


    # ------ DELTA-PHI
    'jetmet_dphi': plot_conf(
        varname = 'jetmet_dphi',
        xtitle = '#Delta#phi(jet, E_{T}^{miss})',
        ytitle = 'Events / BIN',
        legpos = 'top',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'gammet_dphi': plot_conf(
        varname = 'gammet_dphi',
        xtitle = '#Delta#phi(#gamma, E_{T}^{miss})',
        ytitle = 'Events / BIN',
        legpos = 'top',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'dphi': plot_conf(
        varname = 'dphi',
        xtitle = '#Delta#phi',
        ytitle = 'Events / BIN',
        legpos = 'top',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),


    # ------ LEPTONS
    'el_n': plot_conf(
        varname = 'el_n',
        xtitle = 'Number of electrons',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'mu_n': plot_conf(
        varname = 'mu_n',
        xtitle = 'Number of muons',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'el_phi[0]': plot_conf(
        varname = 'el_phi[0]',
        xtitle = 'Leading Electron #phi',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'mu_phi[0]': plot_conf(
        varname = 'mu_phi[0]',
        xtitle = 'Leading Muon #phi',
        ytitle = 'Events / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),


    # ------ OTHERS
    'rt4': plot_conf(
        varname = 'rt4',
        xtitle = 'R_{T}^{4}',
        ytitle = 'Events / BIN',
        legpos = 'left',
        xmin = 0.3,
        xmax = 1.1,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ht0': plot_conf(
        varname = 'ht0',
        xtitle = 'H_{T} (only jets) [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'ht': plot_conf(
        varname = 'ht',
        xtitle = 'H_{T} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),    

    'meff': plot_conf(
        varname = 'meff',
        xtitle = 'm_{eff} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'mt': plot_conf(
        varname = 'mt',
        xtitle = 'M_{T} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),

    'mt_gam': plot_conf(                          
        varname = 'mt_gam',
        xtitle = 'M_{T}^{#gamma} [GeV]',
        ytitle = 'Events / BIN GeV',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),


    # ------ PILEUP
    'avgmu': plot_conf(
        varname = 'avgmu',
        xtitle = '<#mu>',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),

    'mu': plot_conf(
        varname = 'mu',
        xtitle = '#mu',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'NPV': plot_conf(
        varname = 'NPV',
        xtitle = 'N primary vertex',
        ytitle = 'Events',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    
    # ------ STATISTICS
    'chi2': plot_conf(
        varname = 'chi2',
        xtitle = '#chi^{2}',
        ytitle = 'Entries / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'chi2ndof': plot_conf(
        varname = 'chi2ndof',
        xtitle = '#chi^{2} / ndof',
        ytitle = 'Entries / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'pvalue': plot_conf(
        varname = 'pvalue',
        xtitle = 'p-value',
        ytitle = 'Entries / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = True,
    ),
    
    'ftest': plot_conf(
        varname = 'ftest',
        xtitle = 'F-score',
        ytitle = 'Entries / BIN',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    'spurious_signal': plot_conf(
        varname = 'spurious_signal',
        xtitle = '|N_{sig}/#sigma_{N_{sig}}|',
        ytitle = 'Entries',
        legpos = 'right',
        xmin = -1.2,
        xmax = 1.2,
        ymin = None,
        ymax = None,
        logx = True,
        logy = False,
    ),
    
    'signal_events': plot_conf(
        varname = 'signal_events',
        xtitle = 'N_{sig}',
        ytitle = 'Entries',
        legpos = 'right',
        xmin = None,
        xmax = None,
        ymin = None,
        ymax = None,
        logx = False,
        logy = False,
    ),
    
    # ------ CUTFLOWS
    'abseff': plot_conf(
        varname = 'abseff',
        xtitle = '#varepsilon_{abs}',
        ytitle = '#varepsilon_{abs}',
        legpos = 'right',
        xmin = 0,
        xmax = 1.2,
        ymin = 0,
        ymax = 1.2,
        logx = False,
        logy = False,
    ),
}
#===================================================================================================

#===================================================================================================
def get_plotconf(variable: str) -> tuple[plot_conf, plot_conf] | plot_conf:
    if ':' in variable:
        varx, vary = variable.split(':')
        confx = plots_conf.get(varx)
        confy = plots_conf.get(vary)

        if confx is None:
            confx = plots_conf['default']
        if confy is None:
            confy = plots_conf['default']

        return confx, confy
    else:
        return plots_conf.get(variable, plots_conf['default'])
#===================================================================================================