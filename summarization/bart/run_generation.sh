export OUTPUT_DIR_NAME=bart_utest_output
export CURRENT_DIR=${PWD}
export OUTPUT_DIR=${CURRENT_DIR}/${OUTPUT_DIR_NAME}

# Make output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Add parent directory to python path to access lightning_base.py and utils.py
export PYTHONPATH="../../":"${PYTHONPATH}"
python generate_summary_v2.py \
--source_path=cnn_tiny/test.source \
--output_path=$OUTPUT_DIR/generated_title.text \
--model_name=facebook/bart-large-cnn \
--device=cpu \
--bs=5 \