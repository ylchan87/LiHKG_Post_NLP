## What the code does?
Given a LiHKG Post title, predict which sub-forum it is from.
```
In [67]: predict_cat("Annual Dinner 抽中左Dyson 風筒，HR打黎話要收返")

14 上班台 0.70
31 創意台 0.15
 1 吹水台 0.12
30 感情台 0.04
 5 時事台 0.02
```

This repo accompanies the sharing given in https://www.meetup.com/Deep-Learning-HK/events/259092661/

## How to run the notebooks
1. Run `pip install -r requirements.txt` to install allenNLP and pytorch

2. Download BERT pretrained weight and vocab to folder `pretrain` from

    https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-multilingual-cased.tar.gz

    https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-multilingual-cased-vocab.txt


3. Download BERT finetuned (with LiHKG post) weight to folder `chkpoint` from

    https://drive.google.com/file/d/1kmx1CZq0RSFelpVKF6Fb05oRFdN8kQdg/view?usp=sharing

4. run the notebook `code/bert_text_classification_lihkg.ipynb`

## Acknowledgement
This repo borrows a lot from 

https://mlexplained.com/2019/01/30/an-in-depth-tutorial-to-allennlp-from-basics-to-elmo-and-bert/#more-853
