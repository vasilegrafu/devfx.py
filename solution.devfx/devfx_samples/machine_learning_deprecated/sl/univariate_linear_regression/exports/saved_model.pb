�g
��
8
Const
output"dtype"
valuetensor"
dtypetype

NoOp
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
@
ReadVariableOp
resource
value"dtype"
dtypetype�
�
StatefulPartitionedCall
args2Tin
output2Tout"
Tin
list(type)("
Tout
list(type)("	
ffunc"
configstring "
config_protostring "
executor_typestring �
q
VarHandleOp
resource"
	containerstring "
shared_namestring "
dtypetype"
shapeshape�"serve*2.1.02v2.1.0-rc2-17-ge5bf8de4108�[
X
w0VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_namew0
Q
w0/Read/ReadVariableOpReadVariableOpw0*
_output_shapes
: *
dtype0
X
w1VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_namew1
Q
w1/Read/ReadVariableOpReadVariableOpw1*
_output_shapes
: *
dtype0

NoOpNoOp
�
ConstConst"/device:CPU:0*
_output_shapes
: *
dtype0*�
value�B� B�
 
w0
w1

signatures
53
VARIABLE_VALUEw0w0/.ATTRIBUTES/VARIABLE_VALUE
53
VARIABLE_VALUEw1w1/.ATTRIBUTES/VARIABLE_VALUE
 
O
saver_filenamePlaceholder*
_output_shapes
: *
dtype0*
shape: 
�
StatefulPartitionedCallStatefulPartitionedCallsaver_filenamew0/Read/ReadVariableOpw1/Read/ReadVariableOpConst*
Tin
2*
Tout
2*,
_gradient_op_typePartitionedCallUnused*
_output_shapes
: **
config_proto

CPU

GPU 2J 8*'
f"R 
__inference__traced_save_46107
�
StatefulPartitionedCall_1StatefulPartitionedCallsaver_filenamew0w1*
Tin
2*
Tout
2*,
_gradient_op_typePartitionedCallUnused*
_output_shapes
: **
config_proto

CPU

GPU 2J 8**
f%R#
!__inference__traced_restore_46125�Q
�

�
__inference____108

args_0
readvariableop_resource
readvariableop_1_resource
identity��ReadVariableOp�ReadVariableOp_1q
Reshape/shapeConst*
_output_shapes
:*
dtype0*
valueB:
���������2
Reshape/shapek
ReshapeReshapeargs_0Reshape/shape:output:0*
T0*#
_output_shapes
:���������2	
Reshapep
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes
: *
dtype02
ReadVariableOpi
mulMulReadVariableOp:value:0Reshape:output:0*
T0*#
_output_shapes
:���������2
mulv
ReadVariableOp_1ReadVariableOpreadvariableop_1_resource*
_output_shapes
: *
dtype02
ReadVariableOp_1d
addAddV2ReadVariableOp_1:value:0mul:z:0*
T0*#
_output_shapes
:���������2
addu
Reshape_1/shapeConst*
_output_shapes
:*
dtype0*
valueB:
���������2
Reshape_1/shaper
	Reshape_1Reshapeadd:z:0Reshape_1/shape:output:0*
T0*#
_output_shapes
:���������2
	Reshape_1�
IdentityIdentityReshape_1:output:0^ReadVariableOp^ReadVariableOp_1*
T0*#
_output_shapes
:���������2

Identity"
identityIdentity:output:0**
_input_shapes
:���������::2 
ReadVariableOpReadVariableOp2$
ReadVariableOp_1ReadVariableOp_1:& "
 
_user_specified_nameargs_0
�
�
!__inference__traced_restore_46125
file_prefix
assignvariableop_w0
assignvariableop_1_w1

identity_3��AssignVariableOp�AssignVariableOp_1�	RestoreV2�RestoreV2_1�
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*Q
valueHBFBw0/.ATTRIBUTES/VARIABLE_VALUEBw1/.ATTRIBUTES/VARIABLE_VALUE2
RestoreV2/tensor_names�
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueBB B 2
RestoreV2/shape_and_slices�
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0*
_output_shapes

::*
dtypes
22
	RestoreV2X
IdentityIdentityRestoreV2:tensors:0*
T0*
_output_shapes
:2

Identity�
AssignVariableOpAssignVariableOpassignvariableop_w0Identity:output:0*
_output_shapes
 *
dtype02
AssignVariableOp\

Identity_1IdentityRestoreV2:tensors:1*
T0*
_output_shapes
:2

Identity_1�
AssignVariableOp_1AssignVariableOpassignvariableop_1_w1Identity_1:output:0*
_output_shapes
 *
dtype02
AssignVariableOp_1�
RestoreV2_1/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*1
value(B&B_CHECKPOINTABLE_OBJECT_GRAPH2
RestoreV2_1/tensor_names�
RestoreV2_1/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueB
B 2
RestoreV2_1/shape_and_slices�
RestoreV2_1	RestoreV2file_prefix!RestoreV2_1/tensor_names:output:0%RestoreV2_1/shape_and_slices:output:0
^RestoreV2"/device:CPU:0*
_output_shapes
:*
dtypes
22
RestoreV2_19
NoOpNoOp"/device:CPU:0*
_output_shapes
 2
NoOp�

Identity_2Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^NoOp"/device:CPU:0*
T0*
_output_shapes
: 2

Identity_2�

Identity_3IdentityIdentity_2:output:0^AssignVariableOp^AssignVariableOp_1
^RestoreV2^RestoreV2_1*
T0*
_output_shapes
: 2

Identity_3"!

identity_3Identity_3:output:0*
_input_shapes

: ::2$
AssignVariableOpAssignVariableOp2(
AssignVariableOp_1AssignVariableOp_12
	RestoreV2	RestoreV22
RestoreV2_1RestoreV2_1:+ '
%
_user_specified_namefile_prefix
�
�
__inference____119

args_0

args_1"
statefulpartitionedcall_args_1"
statefulpartitionedcall_args_2
identity��StatefulPartitionedCallq
Reshape/shapeConst*
_output_shapes
:*
dtype0*
valueB:
���������2
Reshape/shapek
ReshapeReshapeargs_0Reshape/shape:output:0*
T0*#
_output_shapes
:���������2	
Reshapeu
Reshape_1/shapeConst*
_output_shapes
:*
dtype0*
valueB:
���������2
Reshape_1/shapeq
	Reshape_1Reshapeargs_1Reshape_1/shape:output:0*
T0*#
_output_shapes
:���������2
	Reshape_1�
StatefulPartitionedCallStatefulPartitionedCallReshape:output:0statefulpartitionedcall_args_1statefulpartitionedcall_args_2*
Tin
2*
Tout
2*,
_gradient_op_typePartitionedCallUnused*#
_output_shapes
:���������**
config_proto

CPU

GPU 2J 8*
fR
__inference____1082
StatefulPartitionedCallu
subSub StatefulPartitionedCall:output:0Reshape_1:output:0*
T0*#
_output_shapes
:���������2
subQ
SquareSquaresub:z:0*
T0*#
_output_shapes
:���������2
SquareX
ConstConst*
_output_shapes
:*
dtype0*
valueB: 2
ConstQ
MeanMean
Square:y:0Const:output:0*
T0*
_output_shapes
: 2
Meanu
Reshape_2/shapeConst*
_output_shapes
:*
dtype0*
valueB:
���������2
Reshape_2/shapeo
	Reshape_2ReshapeMean:output:0Reshape_2/shape:output:0*
T0*
_output_shapes
:2
	Reshape_2s
IdentityIdentityReshape_2:output:0^StatefulPartitionedCall*
T0*
_output_shapes
:2

Identity"
identityIdentity:output:0*9
_input_shapes(
&:���������:���������::22
StatefulPartitionedCallStatefulPartitionedCall:& "
 
_user_specified_nameargs_0:&"
 
_user_specified_nameargs_1
�
�
__inference__traced_save_46107
file_prefix!
savev2_w0_read_readvariableop!
savev2_w1_read_readvariableop
savev2_1_const

identity_1��MergeV2Checkpoints�SaveV2�SaveV2_1�
StringJoin/inputs_1Const"/device:CPU:0*
_output_shapes
: *
dtype0*<
value3B1 B+_temp_1d152800c7714c2e98cd47a36097125f/part2
StringJoin/inputs_1�

StringJoin
StringJoinfile_prefixStringJoin/inputs_1:output:0"/device:CPU:0*
N*
_output_shapes
: 2

StringJoinZ

num_shardsConst*
_output_shapes
: *
dtype0*
value	B :2

num_shards
ShardedFilename/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B : 2
ShardedFilename/shard�
ShardedFilenameShardedFilenameStringJoin:output:0ShardedFilename/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: 2
ShardedFilename�
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*Q
valueHBFBw0/.ATTRIBUTES/VARIABLE_VALUEBw1/.ATTRIBUTES/VARIABLE_VALUE2
SaveV2/tensor_names�
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueBB B 2
SaveV2/shape_and_slices�
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:0savev2_w0_read_readvariableopsavev2_w1_read_readvariableop"/device:CPU:0*
_output_shapes
 *
dtypes
22
SaveV2�
ShardedFilename_1/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B :2
ShardedFilename_1/shard�
ShardedFilename_1ShardedFilenameStringJoin:output:0 ShardedFilename_1/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: 2
ShardedFilename_1�
SaveV2_1/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*1
value(B&B_CHECKPOINTABLE_OBJECT_GRAPH2
SaveV2_1/tensor_names�
SaveV2_1/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueB
B 2
SaveV2_1/shape_and_slices�
SaveV2_1SaveV2ShardedFilename_1:filename:0SaveV2_1/tensor_names:output:0"SaveV2_1/shape_and_slices:output:0savev2_1_const^SaveV2"/device:CPU:0*
_output_shapes
 *
dtypes
22

SaveV2_1�
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0ShardedFilename_1:filename:0^SaveV2	^SaveV2_1"/device:CPU:0*
N*
T0*
_output_shapes
:2(
&MergeV2Checkpoints/checkpoint_prefixes�
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix	^SaveV2_1"/device:CPU:0*
_output_shapes
 2
MergeV2Checkpointsr
IdentityIdentityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: 2

Identity�

Identity_1IdentityIdentity:output:0^MergeV2Checkpoints^SaveV2	^SaveV2_1*
T0*
_output_shapes
: 2

Identity_1"!

identity_1Identity_1:output:0*
_input_shapes

: : : : 2(
MergeV2CheckpointsMergeV2Checkpoints2
SaveV2SaveV22
SaveV2_1SaveV2_1:+ '
%
_user_specified_namefile_prefix
�
�
__forward____194
args_0_0
readvariableop_resource
readvariableop_1_resource
identity
add
readvariableop_1
mul
readvariableop
reshape

args_0��ReadVariableOp�ReadVariableOp_1q
Reshape/shapeConst*
_output_shapes
:*
dtype0*
valueB:
���������2
Reshape/shapem
ReshapeReshapeargs_0_0Reshape/shape:output:0*
T0*#
_output_shapes
:���������2	
Reshapep
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes
: *
dtype02
ReadVariableOpF
mul_0MulReadVariableOp:value:0Reshape:output:0*
T02
mulv
ReadVariableOp_1ReadVariableOpreadvariableop_1_resource*
_output_shapes
: *
dtype02
ReadVariableOp_1C
add_0AddV2ReadVariableOp_1:value:0	mul_0:z:0*
T02
addu
Reshape_1/shapeConst*
_output_shapes
:*
dtype0*
valueB:
���������2
Reshape_1/shapet
	Reshape_1Reshape	add_0:z:0Reshape_1/shape:output:0*
T0*#
_output_shapes
:���������2
	Reshape_1�
IdentityIdentityReshape_1:output:0^ReadVariableOp^ReadVariableOp_1*
T0*#
_output_shapes
:���������2

Identity"
add	add_0:z:0"
args_0args_0_0"
identityIdentity:output:0"
mul	mul_0:z:0"(
readvariableopReadVariableOp:value:0",
readvariableop_1ReadVariableOp_1:value:0"
reshapeReshape:output:0**
_input_shapes
:���������::*=
backward_function_name#!__inference___backward____159_1952 
ReadVariableOpReadVariableOp2$
ReadVariableOp_1ReadVariableOp_1:& "
 
_user_specified_nameargs_0"�J
saver_filename:0StatefulPartitionedCall:0StatefulPartitionedCall_18"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp:�
L
w0
w1

signatures
J
h"
_generic_user_object
:
 2w0
:
 2w1
"
signature_map
�2�
__inference____119�
���
FullArgSpec
args�
jself
varargsjargs
varkwjkwargs
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� */�,
����������
����������
�2�
__inference____108�
���
FullArgSpec
args�
jself
varargsjargs
varkwjkwargs
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *�
����������]
__inference____108G+�(
!�
�
args_0���������
� "����������r
__inference____119\I�F
?�<
�
args_0���������
�
args_1���������
� "�