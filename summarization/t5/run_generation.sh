#!/bin/bash

export OUTPUT_DIR_NAME=t5_output
export CURRENT_DIR=${PWD}
export OUTPUT_DIR=${CURRENT_DIR}/${OUTPUT_DIR_NAME}

# Make output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Add parent directory to python path to access lightning_base.py and utils.py
export PYTHONPATH="../../":"${PYTHONPATH}"
python generate_summary.py \
--model_size=$OUTPUT_DIR \
--input_path=$CURRENT_DIR/all_train_test_data/test.source \
--output_path=$OUTPUT_DIR/t5small_fine_tuned_generated_title.text \
--score_path=$OUTPUT_DIR/t5small_fine_tuned_rouge_score.txt \
--reference_path=$CURRENT_DIR/all_train_test_data/test.target 

#model_size, input_path, output_path, reference_path, score_pathinput_path
