# meeting notes

## 2021.10.21

- mel frequency bands, MFCC
- CNN from spectrogram image - ResNet, VGGNet 16 - classifier (image classifier)
  - cut off last layer, 2nd last layer as features
- CRNN models - features from spectrogram
- raw features to embeddings
- Rectified Linear Unit - ReLU

## 2021.10.07

- SVM - use kernel features better accuracy
- fourier signal/transform
- FFT - fast fourier transform
- spectrogram
- MFCC
- get strongly labeled dataset

# research papers

- [Illegal Logging Detection Based on Acoustic
  Surveillance of Forest](https://www.mdpi.com/2076-3417/10/20/7379/pdf) - Piyush
- [Acoustic Signal Classification for Deforestation Monitoring: Tree Cutting
  Problem](https://www.hilarispublisher.com/open-access/acoustic-signal-classification-for-deforestation-monitoring-tree-cutting-problem-jcsb-1000268.pdf) - Manish
- [Automatic detection of tree cutting in forests using acoustic properties](https://doi.org/10.1016/j.jksuci.2019.01.016) - Arpan

# references/links

- [youtube playlist](https://youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0)
  on Audio Signal Processing for Machine Learning
  - slides and jupyter notebooks of the course - <https://github.com/musikalkemist/AudioSignalProcessingForML>
- strongly labelled data - <https://research.google.com/audioset/download_strong.html>
- google sheet for course - <https://docs.google.com/spreadsheets/d/123XoA5jyapDe3X_4IUsoFQ2nh4eEvIMQGKunq0jSohg/edit#gid=987598356>
- onedrive shared folder - <https://iitk-my.sharepoint.com/:f:/g/personal/arpank21_iitk_ac_in/EvIvVuWF8MBPnjMqHDHh3BEBP_XFv5plct9JOqgSyErCOw>
- <https://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html>

# notes from [Automatic detection of tree cutting in forests using acoustic properties](https://doi.org/10.1016/j.jksuci.2019.01.016) - Arpan

- collected from forest and sounddog.com, freesound.org
- extracted features divided into training and test set
- capture acoustic signal -> noise removal using signal analysis software? -> calculate parameter extraction using MATLAB -> classification using algorithms
- 60 tree cutting by axe signals recorded in forest
  - 60 total of balloon burst, hand clap, hammering, digging also collected
  - total 120 signals divided into 5 classes: 60 of axe tree cutting, 60 of the other 4 categories
- 80 kept for training, 40 for testing
- tree cutting signals divided in frames of 10ms
- 5 time domain and 5 frequency domain features used
- 3 algorithms: GMM, K-means clustering, PCA
  - GMM
  - K means clustering
  - PCA
