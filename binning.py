## Histograms binning
binning_dict = dict()

## counts
binning_dict['cuts']    = (1, 0.5, 1.5)
binning_dict['default'] = (100, 0., 1000)

## default for common variables
binning_dict['pt']  = (100, 0, 2000)
binning_dict['eta'] = (100, -3., 3.)
binning_dict['phi'] = (100, -3.4, 3.4)

## photon
binning_dict['ph_n']          = (7, 0, 7)
binning_dict['ph_pt']         = (220, 150., 6000.)  ##(145., 200, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000)
binning_dict['ph_pt[0]']      = (220, 150., 6000.)  ##(145., 200, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000)
binning_dict['ph_pt[1]']      = (220, 150., 6000.)  ##(145., 200, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000)
binning_dict['ph_is_iso']     = (2, 0, 2) # pass isolation
binning_dict['ph_is_iso_ext'] = (2, 0, 2) # pass isolation
binning_dict['ph_iso']        = (100, -20., 80.) # calo isolation
binning_dict['ph_iso[0]']     = (100, -20., 80.) # calo isolation
binning_dict['ph_eta']        = (100, -3., 3.)
binning_dict['abs(ph_eta[0])']= (100, 0., 3.)
binning_dict['ph_eta[0]']     = (100, -3., 3.)
binning_dict['ph_eta[1]']     = (100, -3., 3.)
binning_dict['ph_etas2']      = (100, -3., 3.)
binning_dict['ph_etas2[0]']   = (100, -3., 3.)
binning_dict['ph_etas2[1]']   = (100, -3., 3.)
binning_dict['ph_phi']        = (50, -3.4, 3.4)
binning_dict['ph_phi[0]']     = (50, -3.4, 3.4)
binning_dict['ph_phi[1]']     = (50, -3.4, 3.4)
binning_dict['ph_truth_pt']   = (130, 150., 6000.)
binning_dict['ph_etcone40']   = (50, -5., 20.)
binning_dict['ph_ptcone20']   = (50, -5., 20.)
binning_dict['ph_trackiso']   = (120, 0., 0.3)
binning_dict['ph_type']       = (4, 0, 4)

binning_dict['lph_n']        = (7, 0, 7)
binning_dict['lph_pt']       = (220, 150., 6000.)  ##(145., 200, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000)
binning_dict['lph_pt[0]']    = (220, 150., 6000.)  ##(145., 200, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000)
binning_dict['lph_pt[1]']    = (220, 150., 6000.)  ##(145., 200, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000)
binning_dict['lph_is_iso']   = (2, 0, 2)  # calo isolation
binning_dict['lph_iso']      = (100, -20., 80.) # calo isolation
binning_dict['lph_iso[0]']   = (100, -20., 80.) # calo isolation
binning_dict['lph_eta']      = (100, -3., 3.)
binning_dict['lph_eta[0]']   = (100, -3., 3.)
binning_dict['lph_eta[1]']   = (100, -3., 3.)
binning_dict['lph_etas2']    = (100, -3., 3.)
binning_dict['lph_etas2[0]'] = (100, -3., 3.)
binning_dict['lph_etas2[1]'] = (100, -3., 3.)
binning_dict['lph_phi']      = (50, -3.4, 3.4)
binning_dict['lph_phi[0]']   = (50, -3.4, 3.4)
binning_dict['lph_phi[1]']   = (50, -3.4, 3.4)
binning_dict['lph_id']       = (6, 0., 6.)
binning_dict['lph_etcone40'] = (50, -5., 20.)
binning_dict['lph_ptcone20'] = (50, -5., 20.)
binning_dict['lph_trackiso'] = (120, 0., 0.3)
binning_dict['lph_conv']     = (6, 0, 6)

## jets
binning_dict['jet_n']           = (20, 0, 20)
binning_dict['bjet_n']          = (10, 0, 10)
binning_dict['jet_pt']          = (220, 0., 6000.)
binning_dict['jet_e']           = (40 , 0., 2000.)
binning_dict['jet_eta']         = (100, -4., 4.)
binning_dict['abs(jet_eta[0])'] = (100, 0., 4.)
binning_dict['jet_phi']         = (100, -3.4, 3.4)
binning_dict['jet_isb']         = (7, -1, 5)
binning_dict['jet_pt[0]']       = (220, 0., 6000.)
binning_dict['jet_pt[1]']       = (220, 0., 6000.)
binning_dict['jet_pt[2]']       = (220, 0., 6000.)
binning_dict['jet_eta[0]']      = (100, -3., 3.)
binning_dict['jet_eta[1]']      = (100, -3., 3.)
binning_dict['jet_eta[2]']      = (100, -3., 3.)
binning_dict['jet_phi[0]']      = (50, -3.4, 3.4)
binning_dict['jet_phi[1]']      = (50, -3.4, 3.4)
binning_dict['jet_phi[2]']      = (50, -3.4, 3.4)
binning_dict['jet_btag_pu']     = (100, 0, 1)
binning_dict['jet_btag_pb']     = (100, 0, 1)
binning_dict['jet_btag_pc']     = (100, 0, 1)
binning_dict['jet_btag_w']      = (100, -10, 10)
binning_dict['dl1d_b']          = (100, -10, 10)
binning_dict['dl1d_c']          = (100, -10, 10)
# =0: lightjet
# =4: c-jet
# =5: b-jet
binning_dict['jet_truthflavorid'] = (6, 0, 6)
binning_dict['jetjet_m']          = (50, 0, 1500)

## photon+jet
binning_dict['phjet_m']     = (10000, 0., 10000.)
binning_dict['phjet_pt']    = (220, 0., 6000.)
binning_dict['phjet_et']    = (220, 0., 6000.)
binning_dict['phjet_eta']   = (100, -7. , 7.)
binning_dict['phjet_phi']   = (100, -3.4, 3.4)
binning_dict['phjet_dphi']  = (60, 0., 3.4)
binning_dict['phjet_deta']  = (60, 0., 6.)
binning_dict['phjet_dr']    = (60, 0., 6.)
binning_dict['phjet_dr_min']= (60, 0., 6.)
binning_dict['phjet_drmin'] = (60, 0., 6.)
binning_dict['phjet_pt/phjet_m'] = (100, 0., 1)
binning_dict['ph_pt[0]/phjet_m'] = (100, 0., 1)
binning_dict['ph_pt/phjet_m']    = (100, 0., 1)


## met
binning_dict['met_et']        = (10, 0, 1000)
# binning_dict['met_noele_et']  = (10, 0, 1000)
# binning_dict['met_nomuon_et'] = (10, 0, 1000)
# binning_dict['met_et']        = (20, 0, 1000)
# binning_dict['met_et']        = (100, 200, 300, 400, 500, 600, 1000) #SRH
# binning_dict['met_et']        = (100, 250, 500, 750) #SRL
# binning_dict['met_et']        = (100, 300, 500, 750) #srm
# binning_dict['met_et']        = (100, 250, 400, 600, 1000) #SRH
binning_dict['met_phi']       = (17, -3.4, 3.4)
# binning_dict['met_soft_et']   = (20, 0., 500.)
# binning_dict['met_soft_et']   = (20, 0., 1000.)
# binning_dict['met_soft_phi']  = (17, -3.4, 3.4)
binning_dict['met_ph_et']    = (20, 0., 1000.)
binning_dict['met_ph_phi']   = (17, -3.4, 3.4)
binning_dict['met_jet_et']   = (20, 0., 1000.)
binning_dict['met_jet_phi']  = (17, -3.4, 3.4)
# binning_dict['met_ele_et']    = (20, 0., 1000.)
# binning_dict['met_ele_phi']   = (17, -3.4, 3.4)
# binning_dict['met_muon_et']   = (20, 0., 1000.)
# binning_dict['met_muon_phi']  = (17, -3.4, 3.4)
# binning_dict['met_track_et']  = (20, 0., 1000.)
# binning_dict['met_track_phi'] = (17, -3.4, 3.4)
binning_dict['met_sig']       = (50, 0., 50.)
binning_dict['met_sumet']     = (40, 0., 8000.)
binning_dict['met_truth_et']  = (20, 0., 1000.)

## dphi
binning_dict['jetmet_dphi']   = (17, 0., 3.4)
binning_dict['gammet_dphi']   = (17, 0., 3.4)
binning_dict['dphi']          = (17, 0., 3.4)
# binning_dict['dphi_gamsoft']  = (17, 0., 3.4)
# binning_dict['get_dphi(ph_phi[0], met_soft_phi)'] = (17, 0., 3.4)

## leptons
binning_dict['el_n']      = (10, 0, 10)
binning_dict['mu_n']      = (10, 0, 10)
binning_dict['el_phi[0]'] = (34, -3.4, 3.4)
binning_dict['mu_phi[0]'] = (34, -3.4, 3.4)

## others
binning_dict['ht0']             = (30, 0., 6000.)
# binning_dict['ht']              = (15, 0., 3000.)
# binning_dict['ht']              = (30, 0., 3000.)
binning_dict['ht']              = (30, 0., 6000.)
binning_dict['meff']            = (12, 0., 6000.)
# binning_dict['meff']            = (15, 0., 6000.)
# binning_dict['rt1']             = (22, 0., 1.1)
# binning_dict['rt2']             = (22, 0., 1.1)
# binning_dict['rt3']             = (22, 0., 1.1)
binning_dict['rt4']             = (22, 0., 1.1)
binning_dict['mt']              = (50, 0, 2500.)
binning_dict['mt_gam']          = (60, 0, 1500.)
# binning_dict['mt2']             = (50, 0, 15000.)
# binning_dict['stgam']           = (25, 0, 5000.)
# binning_dict['met_et/sqrt(ht)'] = (100, 0., 50.)
# binning_dict['met_et/meff']     = (20, 0., 1.)
# binning_dict['met_et/ht']       = (40, 0., 2.)
# binning_dict['ht/meff']         = (20, 0., 1.)
# binning_dict['ph_pt[0]+met_et'] = (25, 0, 5000.)
# binning_dict['ht+met_et']       = (50, 0, 5000.)
# binning_dict['ht+met_et-ph_pt'] = (60, 0, 6000.)
# binning_dict['ht-ph_pt[0]']     = (25, 0, 5000.)


## weights
binning_dict['weight_mc']       = (100, -0.5, 3.0)
binning_dict['weight_pu']       = (100, -0.5, 3.0)
binning_dict['weight_sf']       = (100, -0.5, 3.0)
binning_dict['weight_lumi']     = (100, -0.5, 3.0)

## pileup
binning_dict['NPV']             = (100, 0, 100)
binning_dict['mu']              = (80, 0, 80)
binning_dict['avgmu']           = (80, 0, 80)

## triggers
binning_dict['pass_g140']       = (2, 0, 2)

## statistics
binning_dict['chi2']     = (100, 0, 2000)
binning_dict['chi2ndof'] = (50 , 0, 10)
binning_dict['ftest']    = (200, 0, 400)
binning_dict['pvalue']   = (100, 0, 1)
