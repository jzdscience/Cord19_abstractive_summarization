#!usr/bin/env bash

export OUTPUT_DIR_NAME=output/all_data_bart
export CURRENT_DIR=${PWD}
export OUTPUT_DIR=${CURRENT_DIR}/${OUTPUT_DIR_NAME}

# Make output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Add parent directory to python path to access lightning_base.py and utils.py
export PYTHONPATH="../../":"${PYTHONPATH}"
python generate_summary_v2.py \
--source_path=all_train_test_data/test.source \
--output_path=$OUTPUT_DIR/bart_tiny_untuned_generated_title.text \
--model_name=sshleifer/bart-tiny-random \
--device=cuda \
--bs=5 \
