# Since our default folder structure is task/seed/algo/experiment_name/datetime,
# we have algo/experiment_name for each task/algo combo

algo_dir_names = ['multi-sqil', 'multi-disc', 'multi-rce', 'sqil', 'dac', 'rce']

main_performance = {
    'sawyer_drawer_open': {
        # 'multi-sqil':        "multi-sqil/mar3",
        'multi-sqil':        "multi-sqil/mar8_reachandgrasp",
        # 'multi-disc':        "multi-disc/mar3",
        'multi-disc':        "multi-disc/mar8_reachandgrasp",
        'sqil':              "sqil/mar3",
        'rce':               "rce/mar3",
        # 'rce_orig':          "rce/mar3_rce_orig",
        'rce_orig':          "rce_theirs/mar23",
        'sqil_theirs':          "sqil_theirs/mar27",
        'disc':              "disc/mar31",
        'multi-rce':         "multi-rce/mar31",
        'sqil_theirs_nstepoff': "sqil_theirs_nstepoff/apr1",
        'multi-sqil-no-vp':          "multi-sqil/apr4_noqovermax",
        'sqil-no-vp':        "sqil/apr4_noqovermax",
    },
    'sawyer_drawer_close': {
        'multi-sqil':        "multi-sqil/mar10",
        'multi-disc':        "multi-disc/mar10",
        'sqil':              "sqil/mar10",
        'rce':               "rce/mar10",
        # 'rce_orig':          "rce/mar10_rce_orig",
        'rce_orig':          "rce_theirs/mar23",
        'sqil_theirs':          "sqil_theirs/mar27",
        'disc':              "disc/mar31",
        'multi-rce':         "multi-rce/mar31",
        'sqil_theirs_nstepoff': "sqil_theirs_nstepoff/apr1",
        'multi-sqil-no-vp':          "multi-sqil/apr4_noqovermax",
        'sqil-no-vp':        "sqil/apr4_noqovermax",
    },
    'sawyer_push': {
        # 'multi-sqil':        "multi-sqil/mar3",
        'multi-sqil':        "multi-sqil/mar5_graspfixeddefaults",
        'multi-disc':        "multi-disc/mar5_graspfixeddefaults",
        # 'sqil':              "sqil/mar3",
        'sqil':              "sqil/mar5_graspfixeddefaults",
        'rce':               "rce/mar5_graspfixeddefaults",
        # 'rce_orig':          "rce/mar5_graspfixeddefaults_rce_orig",
        'rce_orig':          "rce_theirs/mar23",
        'sqil_theirs':          "sqil_theirs/mar27",
        'disc':              "disc/mar31",
        'multi-rce':         "multi-rce/mar31",
        'sqil_theirs_nstepoff': "sqil_theirs_nstepoff/apr1",
        'multi-sqil-no-vp':          "multi-sqil/apr4_noqovermax",
        'sqil-no-vp':        "sqil/apr4_noqovermax",
    },
    'sawyer_lift': {
        # 'multi-sqil':        "multi-sqil/mar3",
        # 'multi-sqil':        "multi-sqil/mar5_withgrasp_2hcopts_xynoiseexp_tau5e-3_FIXED",
        'multi-sqil':        "multi-sqil/mar5_withgrasp_2hcopts_xynoiseexp",
        'multi-disc':        "multi-disc/mar5_withgrasp_2hcopts_xynoiseexp",
        # 'sqil':              "sqil/mar3",
        # 'sqil':              "sqil/mar5_withgrasp_2hcopts_xynoiseexp_tau5e-3_FIXED",
        'sqil':              "sqil/mar5_withgrasp_2hcopts_xynoiseexp",
        'rce':               "rce/mar5_withgrasp_2hcopts_xynoiseexp",
        # 'rce_orig':          "rce/mar5_withgrasp_2hcopts_xynoiseexp_rce_orig",
        'rce_orig':          "rce_theirs/mar23",
        'sqil_theirs':          "sqil_theirs/mar27",
        'disc':              "disc/mar31",
        'multi-rce':         "multi-rce/mar31",
        'sqil_theirs_nstepoff': "sqil_theirs_nstepoff/apr1",
        'multi-sqil-no-vp':          "multi-sqil/apr4_noqovermax",
        'sqil-no-vp':        "sqil/apr4_noqovermax",
    },
    'sawyer_box_close': {
        'multi-sqil':        "multi-sqil/mar5_graspfixeddefaults",
        'multi-disc':        "multi-disc/mar5_graspfixeddefaults",
        'sqil':              "sqil/mar5_graspfixeddefaults",
        'rce':               "rce/mar5_graspfixeddefaults",
        # 'rce_orig':          "rce/mar5_graspfixeddefaults_rce_orig",
        'rce_orig':          "rce_theirs/mar23",
        'sqil_theirs':          "sqil_theirs/mar27",
        'disc':              "disc/mar31",
        'multi-rce':         "multi-rce/mar31",
        'sqil_theirs_nstepoff': "sqil_theirs_nstepoff/apr1",
        'multi-sqil-no-vp':          "multi-sqil/apr4_noqovermax",
        'sqil-no-vp':        "sqil/apr4_noqovermax",
    },
    'sawyer_bin_picking': {
        # 'multi-sqil':        "multi-sqil/mar5_graspfixeddefaults",
        # 'multi-disc':        "multi-disc/mar5_graspfixeddefaults",
        # 'sqil':              "sqil/mar5_graspfixeddefaults",
        # 'rce':               "rce/mar5_graspfixeddefaults",
        'rce_orig':          "rce_theirs/mar23",
        'sqil_theirs':          "sqil_theirs/mar27",
        # 'disc':              "disc/mar31",
        # 'multi-rce':         "multi-rce/mar31",
        'sqil_theirs_nstepoff': "sqil_theirs_nstepoff/apr1",
        # 'multi-sqil-no-vp':          "multi-sqil/apr4_noqovermax",
        # 'sqil-no-vp':        "sqil/apr4_noqovermax",

        'multi-sqil':       "multi-sqil/apr29_datafix",
        'multi-disc':       "multi-disc/apr29_datafix",
        'multi-sqil-no-vp':       "multi-sqil/apr29_datafix_noqovermax",
        'multi-rce':        "multi-rce/apr29_datafix",
        'sqil':             "sqil/apr29_datafix",
        'disc':             "disc/apr29_datafix",
        'rce':              "rce/apr29_datafix",
        'sqil-no-vp':       "sqil/apr29_datafix_noqovermax",
        'multi-sqil':       "multi-sqil/apr29_datafix",
    },
}
