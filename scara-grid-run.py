
#scara grid run 30 fps (2 animals): uncovered-cray-992
grid run --dockerfile Dockerfile --datastore_name emg-data-05-30fps-2an \
--instance_type p3.2xlarge --localdir -- grid-hpo.sh \
--script scripts/train_hydra.sh \
--config-path configs_scara-emg-30fps-2an \
--config-name config_scara-emg-30fps-2an \
--training.train_frames "[1]" \
--model.do_context "[False]" \
--model.model_name "scara-emg-30fps-2an" \
--model.losses_to_use "['[]', '[temporal]','[pca_singleview]']" \
--training.rng_seed_data_pt "[2]" \
--eval.predict_vids_after_training "[True]" \
--eval.save_vids_after_training "[True]"

#scara grid run 30fps (2 animals) w/ context: armored-ishizaka-8703 (150 frames)
grid run --dockerfile Dockerfile --datastore_name emg-data-05-30fps-2an-ctx \
--instance_type p3.2xlarge --localdir -- grid-hpo.sh \
--script scripts/train_hydra.sh \
--config-path configs_scara-emg-30fps-2an-ctx \
--config-name config_scara-emg-30fps-2an-ctx \
--training.train_frames "[1]" \
--model.do_context "[True, False]" \
--model.model_name "scara-emg-30fps-2an-context" \
--model.losses_to_use "['[]']" \
--training.rng_seed_data_pt "[2]" \
--eval.predict_vids_after_training "[True]" \
--eval.save_vids_after_training "[True]"


grid run --dockerfile Dockerfile --datastore_name emg-data-30fps-2an \
--instance_type p3.2xlarge --localdir -- grid-hpo.sh \
--script scripts/train_hydra.sh \
--config-path configs_scara-emg-30fps-2an \
--config-name config_scara-emg-30fps-2an \
--training.train_frames "[1]" \
--model.do_context "[False]" \
--model.model_name "emg-30fps-2an" \
--model.losses_to_use "['[]','[temporal]','[pca_singleview]']" \
--training.rng_seed_data_pt "[2]" \
--eval.predict_vids_after_training "[True]" \
--eval.save_vids_after_training "[True]"