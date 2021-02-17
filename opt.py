class opt:
  expID = 'default'
  dataset = 'coco'
  nThreads = 30
  debug = False
  snapshot = 1
  addDPG = False
  sp = False
  profile = False
  netType = 'hgPRM'
  loadModel = None
  Continue = False
  nFeats = 256
  nClasses = 33
  nStack = 4
  fast_inference = True
  use_pyranet = True
  LR = 2.5e-4
  momentum = 0
  weightDecay = 0
  crit = 'MSE'
  optMethod = 'rmsprop'
  nEpochs = 50
  epoch = 0
  trainBatch = 40
  validBatch = 20
  trainIters = 0
  valIters = 0
  init = None
  inputResH = 320
  inputResW = 256
  outputResH = 80
  outputResW = 64
  scale = 0.25
  rotate = 30
  hmGauss = 1
  baseWidth = 9
  cardinality = 5
  nResidual = 1
  dist = 1
  backend = 'gloo'
  demo_net = 'res152'
  inputpath = ''
  inputlist = ''
  mode = 'normal'
  outputpath = 'examples/res/'
  inp_dim = '608'
  confidence = 0.05
  nms_thesh = 0.6
  save_img = False
  vis = False
  matching = False
  detbatch = 1
  posebatch = 80
  video = ''
  webcam = '0'
  save_video = False
  vis_fast = False
  num_classes = 80
