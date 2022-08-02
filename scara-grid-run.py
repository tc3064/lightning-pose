
#scara grid run 2
grid run --dockerfile Dockerfile --datastore_name emg-data-04 \
--instance_type p3.2xlarge --localdir -- grid-hpo.sh \
--script scripts/train_hydra.sh \
--config-path configs_scara-emg \
--config-name config_scara-emg \
--training.train_frames "[75,1]" \
--model.do_context "[False]" \
--model.model_name "scara-emg-temp-pca" \
--model.losses_to_use "['[temporal]','[pca_singleview]']" \
--training.rng_seed_data_pt "[1,2]" \
--eval.predict_vids_after_training "[True]" \
--eval.save_vids_after_training "[False]"