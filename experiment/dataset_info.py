import os
data_path = "/Users/berkkayi/Desktop/aws_data_engineering_masterclass/dataset/raw_data"
#listing all data from dataset path
total_size = 0
for dataset in os.listdir(data_path):
    # getsize return as a byte. 
    size = os.path.getsize(data_path + "/" + dataset)
    print(dataset," size is : ",round(size/(1024*1024), 2)," MB")
    total_size += size

print("\ntotal size is : ",round(total_size/(1024*1024*1024), 3)," GB")
