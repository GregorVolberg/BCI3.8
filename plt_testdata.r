library(tidyverse)

#eeg <- read_delim("./testData_250Hz.csv", col_names = FALSE) %>%
# bei cyton ist Kanal 24 der Markerkanal
# bei synthetic ist 32 der Markerkanal
eeg <- read_delim("./syntheticTest_250Hz.csv", col_names = FALSE) %>%
    select(X2:X9, X32) %>%
  mutate(point = 1:nrow(.),
         s = point * 1/250) %>%
  select(point, s, "Fp2" = X2, "FP2" = X3, "Fpz" = X4,
         "P7" = X5, "TP8" = X6, "P8" = X7, "Oz" = X8, 
         "TP7" = X9, "marker" = X32)
  
plot(eeg$s, eeg$marker, type='l')
  
