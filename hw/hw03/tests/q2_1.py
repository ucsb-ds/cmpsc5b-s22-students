test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> # Your resample should have the same number of rows as the original sample\n>>> simulate_resample(observations).num_rows == 17\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Your resample should only have the same first label\n>>> simulate_resample(observations).labels[0] == observations.labels[0]\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}