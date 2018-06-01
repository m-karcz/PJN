#!/bin/bash
./fastText-0.1.0/fasttext supervised -input data.train -output tag_polska_model
./fastText-0.1.0/fasttext test tag_polska_model.bin data.valid
