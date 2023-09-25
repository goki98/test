import tensorflow as tf
# initilation of tensors
x=tf.constant(4.5,shape=(1,1),dtype=tf.float32) # a scalar with value 4 and dimensions of matrix is 1 x 1 and data type is float 
y=tf.constant([[1,2,3],[4,5,6]],shape=(2,3),dtype=tf.int32) # a 2 x 3 matrix with elements 1 to 6 , interger data type
z= tf.ones(3,3) # 3 x 3 matrix full of 1 
I= tf.eye(3) # 3 x 3 identity matrix
 
print(x)
print("the 2 x 3 matrix informataion is ",y)  
print ("the unity matrix is ",z)

print("all ok!!")