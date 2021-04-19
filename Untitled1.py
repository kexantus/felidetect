#!/usr/bin/env python
# coding: utf-8

# In[36]:


import noisereduce as nr
import librosa
from scipy.io import wavfile as wav


# In[32]:


# load audio file
Aj1 = 'C:/Users/Karen Exantus/Desktop/Felidae/Acinonyx_jubatus_S0612_02.wav'

audio_data, sampling_rate = librosa.load(Aj1)


# In[39]:


# select section of data that is noise
noise = audio_data[45:49]


# In[34]:


# perform noise reduction
reduced_noise = nr.reduce_noise(audio_clip=audio_data, noise_clip=man_speaking, verbose=True)


# In[ ]:





# In[ ]:




