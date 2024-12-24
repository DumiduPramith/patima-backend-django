#!/bin/bash

# Function to download a file to a specified path
download_file() {
    local target_path="$1"
    local file_url="$2"

    # Check if arguments are provided
    if [ -z "$target_path" ] || [ -z "$file_url" ]; then
        echo "Error: Missing arguments."
        echo "Usage: download_file <target_path> <file_url>"
        return 1
    fi

    # Check if the target path exists
    if [ -d "$target_path" ]; then
        echo "Path exists: $target_path"
    else
        echo "Path does not exist. Creating path: $target_path"
        mkdir -p "$target_path"
        if [ $? -ne 0 ]; then
            echo "Failed to create directory. Exiting."
            return 1
        fi
    fi

    # Download the file
    echo "Downloading file from $file_url..."
    curl -o "${target_path}/$(basename "$file_url")" "$file_url"
    if [ $? -eq 0 ]; then
        echo "File downloaded successfully to $target_path."
    else
        echo "Failed to download file. Please check the URL."
        return 1
    fi
}

# Example usage: Download multiple files
download_file "django-app/prediction/ml_models/segmentation" "https://objectstorage.ap-mumbai-1.oraclecloud.com/n/bmgr1pj5cyeh/b/patima-bucket/o/best.pt"
download_file "django-app/prediction/ml_models/segmentation" "https://objectstorage.ap-mumbai-1.oraclecloud.com/n/bmgr1pj5cyeh/b/patima-bucket/o/unet_best_model_3.keras"
download_file "django-app/prediction/ml_models/new_method/checkpoint" "https://objectstorage.ap-mumbai-1.oraclecloud.com/n/bmgr1pj5cyeh/b/patima-bucket/o/checkpoint%2Fcheckpoint"
download_file "django-app/prediction/ml_models/new_method/checkpoint" "https://objectstorage.ap-mumbai-1.oraclecloud.com/n/bmgr1pj5cyeh/b/patima-bucket/o/checkpoint%2Fckpt-8.data-00000-of-00001"
download_file "django-app/prediction/ml_models/new_method/checkpoint" "https://objectstorage.ap-mumbai-1.oraclecloud.com/n/bmgr1pj5cyeh/b/patima-bucket/o/checkpoint%2Fckpt-8.index"
