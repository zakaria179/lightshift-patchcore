# Hypotheses

## QR1. Where does the performance drop come from?

Hypothesis (from the brief): the drift of channel statistics (mean, std) is strongly correlated with the drop in AUROC and AU-PRO as shift severity increases.

**My prediction:** As shift severity increases, the difference between source and target channel statistics (mean and standard deviation) will also increase. I expect this statistical drift to be strongly correlated with the degradation of AUROC and AU-PRO. Larger distribution shifts should generally lead to larger performance drops.

**I would be wrong if:** AUROC and AU-PRO decrease significantly without a corresponding increase in channel-statistics drift, or if large statistical drift occurs while performance remains stable. A weak or inconsistent correlation would also contradict this hypothesis.

## QR2. Ranking vs calibration?

Hypothesis: under lighting shift, AUROC drops a little, but F1 at the source threshold collapses.

**My prediction:** Under lighting shifts, the model will largely preserve its ability to rank normal and anomalous samples, resulting in a relatively small AUROC drop. However, the anomaly-score distribution will shift, making the original source threshold unsuitable and causing a much larger decrease in F1.

**I would be wrong if:** AUROC decreases as much as F1, F1 remains relatively stable at the source threshold, or the observed F1 degradation cannot be explained by a change in the anomaly-score distribution.

## QR3. Which brick helps with what?

Hypothesis: B2 mostly restores ranking, B3 mostly restores calibration, B1 helps but makes the memory bank bigger.

**My prediction:** B2 will produce the largest improvement in ranking-related performance, particularly AUROC. B3 will provide the largest improvement in score calibration and threshold-based performance, particularly F1. B1 will also improve detection performance, but its gains will come with a noticeable increase in memory-bank size and memory consumption.

**I would be wrong if:** B2 does not produce a stronger improvement in AUROC than the other bricks, B3 does not improve calibration or threshold-based metrics, or B1 does not provide a measurable performance gain relative to its additional memory cost.

## QR4. How many target images are needed?

Hypothesis: about 5 to 20 images are enough for B2 and B3. Below that, variance explodes.

**My prediction:** I expect B2 and B3 to achieve most of their adaptation benefits using approximately 5 to 20 target images. With fewer than 5 images, results will be more sensitive to the selected samples and show high variability across repeated experiments. Beyond 20 images, additional performance gains should become smaller.

**I would be wrong if:** B2 and B3 require substantially more than 20 target images to achieve stable improvements, or if using fewer than 5 images consistently produces stable results with low variability.

## QR5. What is the cost?

Hypothesis: B2/B3 add negligible latency and memory, B1 adds noticeable cost.

**My prediction:** B2 and B3 will introduce only minor inference-latency and memory overhead compared with the baseline model. B1 will introduce a more noticeable memory cost because it increases the memory-bank size, and may also increase inference latency.

**I would be wrong if:** B2 or B3 introduce substantial latency or memory overhead, or if B1 increases the memory-bank size without producing a measurable increase in memory consumption or inference cost.

## QR6. What are the limits?

Hypothesis: the methods fail on non-photometric shifts (blur, perspective) and on logical anomalies.

**My prediction:** The proposed methods will be more effective against photometric shifts, such as changes in brightness, contrast, and color, than against non-photometric shifts such as blur and perspective changes. I also expect limited improvements on logical anomalies, which require understanding spatial relationships and structural consistency rather than only low-level visual features.

**I would be wrong if:** The methods achieve comparable improvements on blur, perspective changes, and logical anomalies as they do on photometric shifts, or if they consistently handle these challenging cases without significant performance degradation.
