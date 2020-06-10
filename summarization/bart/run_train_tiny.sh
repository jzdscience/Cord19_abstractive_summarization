#!/bin/bash


# Script for verifying that run_bart_sum can be invoked from its directory

# Get tiny dataset with cnn_dm format (4 examples for train, val, test)
# wget https://s3.amazonaws.com/datasets.huggingface.co/summarization/cnn_tiny.tgz
# tar -xzvf cnn_tiny.tgz
# rm cnn_tiny.tgz

export OUTPUT_DIR_NAME=output/tiny_cnn
export CURRENT_DIR=${PWD}
export OUTPUT_DIR=${CURRENT_DIR}/${OUTPUT_DIR_NAME}

if [ -d "$OUTPUT_DIR" ]; then rm -Rf $OUTPUT_DIR; fi

# Make output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Add parent directory to python path to access lightning_base.py and utils.py
export PYTHONPATH="../../":"${PYTHONPATH}"
python finetune.py \
--data_dir=cnn_tiny/ \
--model_name_or_path=sshleifer/bart-tiny-random \
--learning_rate=1e-2 \
--train_batch_size=2 \
--eval_batch_size=2 \
--output_dir=$OUTPUT_DIR \
--num_train_epochs=5  \
--n_gpu=1  \
--do_train \
--do_predict $@

#--model_name_or_path=sshleifer/bart-tiny-random \

#rm -rf cnn_tiny
#rm -rf $OUTPUT_DIR



