Combine Grid HPO with Hydra Multirun

The process:

- Instead of using `grid run real_script_name.py`
- Proxy the real script using [scripts/grid-hpo.sh](scripts/grid-hpo.sh)
- Prepare the proxy script that has real_script_name.py
- The proxy will execute `grid run scripts/grid-hpo.sh --script proxy.sh`
- Grid HPO params will be added to the real script via the proxy.sh

# Review examples of proxy scripts

## test locally

- read config file and perform local test

```
python scripts/hydra-conf-read-test.py
# will still work but not correct
python scripts/hydra-conf-read-test.py --config-dir scripts/configs_mirror-mouse  --config-name config
python scripts/hydra-conf-read-test.py --config-dir scripts --config-name config
```

- correctly way to read the config

```
python scripts/hydra-conf-read-test.py --config-path configs --config-name config
python scripts/hydra-conf-read-test.py --config-path configs_mirror-mouse --config-name config_mirror-mouse
```

## grid run

- config dir and config path test

```
grid run --instance_type t2.medium --localdir -- grid-hpo.sh --script scripts/hydra-conf-read-test.sh --config-dir "['scripts/configs_mirror-mouse', 'script/configs']" --config-name "['config','config_mirror-mouse']"
```

- config path test with trailing hydra param

```
grid run --instance_type t2.medium --localdir -- grid-hpo.sh --script scripts/hydra-conf-read-test.sh --config-path "['configs_mirror-mouse', 'configs']" --config-name "['config','config_mirror-mouse']" --training.rng_seed_data_pt "[1,2]"
```

- config path test w/o trailing hydra param

```
grid run --instance_type t2.medium --localdir -- grid-hpo.sh --script scripts/hydra-conf-read-test.sh --config-path "['configs_mirror-mouse', 'configs']" --config-name "['config','config_mirror-mouse']"
```

- actual run

```
grid run --dockerfile Dockerfile --instance_type g4dn.xlarge --localdir -- grid-hpo.sh --script scripts/train_hydra.sh --config-path "['configs_mirror-mouse', 'configs']" --config-name "['config','config_mirror-mouse']" --training.rng_seed_data_pt "[1,2]"
```


# run on grid - scara emg 
grid run --name scara-emg-test --dockerfile Dockerfile \
--localdir \
--datastore_name emg-data-03 -- \ 
scripts/grid-hpo.sh \
--script scripts/grid-run-test-emg.sh \
--config-path configs_scara-emg \
--config-name configs_scara-emg \
--training.train_frames "[75,1]" \
--model.do_context "[False]" \
--model.losses_to_use "["pca_singleview"]" \
--training.rng_seed_data_pt "[0,1,2]" \
--losses.pca_singleview.log_weight "[5.0]"
```
