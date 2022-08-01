python scripts/train_hydra.py \
--multirun \
training.train_batch_size=8 \
model.model_name="test_sweep" \
dali.base.train.sequence_length=32 \