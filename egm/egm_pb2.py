# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: egm.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tegm.proto\x12\x07\x61\x62\x62.egm\"\xeb\x01\n\tEgmHeader\x12\r\n\x05seqno\x18\x01 \x01(\r\x12\n\n\x02tm\x18\x02 \x01(\r\x12@\n\x05mtype\x18\x03 \x01(\x0e\x32\x1e.abb.egm.EgmHeader.MessageType:\x11MSGTYPE_UNDEFINED\"\x80\x01\n\x0bMessageType\x12\x15\n\x11MSGTYPE_UNDEFINED\x10\x00\x12\x13\n\x0fMSGTYPE_COMMAND\x10\x01\x12\x10\n\x0cMSGTYPE_DATA\x10\x02\x12\x16\n\x12MSGTYPE_CORRECTION\x10\x03\x12\x1b\n\x17MSGTYPE_PATH_CORRECTION\x10\x04\"/\n\x0c\x45gmCartesian\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\"?\n\rEgmQuaternion\x12\n\n\x02u0\x18\x01 \x02(\x01\x12\n\n\x02u1\x18\x02 \x02(\x01\x12\n\n\x02u2\x18\x03 \x02(\x01\x12\n\n\x02u3\x18\x04 \x02(\x01\"+\n\x08\x45gmEuler\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\"%\n\x08\x45gmClock\x12\x0b\n\x03sec\x18\x01 \x02(\x04\x12\x0c\n\x04usec\x18\x02 \x02(\x04\"w\n\x07\x45gmPose\x12\"\n\x03pos\x18\x01 \x01(\x0b\x32\x15.abb.egm.EgmCartesian\x12&\n\x06orient\x18\x02 \x01(\x0b\x32\x16.abb.egm.EgmQuaternion\x12 \n\x05\x65uler\x18\x03 \x01(\x0b\x32\x11.abb.egm.EgmEuler\"\"\n\x11\x45gmCartesianSpeed\x12\r\n\x05value\x18\x01 \x03(\x01\"\x1b\n\tEgmJoints\x12\x0e\n\x06joints\x18\x01 \x03(\x01\"#\n\x11\x45gmExternalJoints\x12\x0e\n\x06joints\x18\x01 \x03(\x01\"\xa2\x01\n\nEgmPlanned\x12\"\n\x06joints\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmJoints\x12#\n\tcartesian\x18\x02 \x01(\x0b\x32\x10.abb.egm.EgmPose\x12*\n\x0e\x65xternalJoints\x18\x03 \x01(\x0b\x32\x12.abb.egm.EgmJoints\x12\x1f\n\x04time\x18\x04 \x01(\x0b\x32\x11.abb.egm.EgmClock\"\x8d\x01\n\x0b\x45gmSpeedRef\x12\"\n\x06joints\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmJoints\x12.\n\ncartesians\x18\x02 \x01(\x0b\x32\x1a.abb.egm.EgmCartesianSpeed\x12*\n\x0e\x65xternalJoints\x18\x03 \x01(\x0b\x32\x12.abb.egm.EgmJoints\">\n\x0b\x45gmPathCorr\x12\"\n\x03pos\x18\x01 \x02(\x0b\x32\x15.abb.egm.EgmCartesian\x12\x0b\n\x03\x61ge\x18\x02 \x02(\r\"\xa3\x01\n\x0b\x45gmFeedBack\x12\"\n\x06joints\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmJoints\x12#\n\tcartesian\x18\x02 \x01(\x0b\x32\x10.abb.egm.EgmPose\x12*\n\x0e\x65xternalJoints\x18\x03 \x01(\x0b\x32\x12.abb.egm.EgmJoints\x12\x1f\n\x04time\x18\x04 \x01(\x0b\x32\x11.abb.egm.EgmClock\"\x8c\x01\n\rEgmMotorState\x12\x34\n\x05state\x18\x01 \x02(\x0e\x32%.abb.egm.EgmMotorState.MotorStateType\"E\n\x0eMotorStateType\x12\x14\n\x10MOTORS_UNDEFINED\x10\x00\x12\r\n\tMOTORS_ON\x10\x01\x12\x0e\n\nMOTORS_OFF\x10\x02\"\xa2\x01\n\x0b\x45gmMCIState\x12?\n\x05state\x18\x01 \x02(\x0e\x32!.abb.egm.EgmMCIState.MCIStateType:\rMCI_UNDEFINED\"R\n\x0cMCIStateType\x12\x11\n\rMCI_UNDEFINED\x10\x00\x12\r\n\tMCI_ERROR\x10\x01\x12\x0f\n\x0bMCI_STOPPED\x10\x02\x12\x0f\n\x0bMCI_RUNNING\x10\x03\"\xc3\x01\n\x15\x45gmRapidCtrlExecState\x12U\n\x05state\x18\x01 \x02(\x0e\x32\x35.abb.egm.EgmRapidCtrlExecState.RapidCtrlExecStateType:\x0fRAPID_UNDEFINED\"S\n\x16RapidCtrlExecStateType\x12\x13\n\x0fRAPID_UNDEFINED\x10\x00\x12\x11\n\rRAPID_STOPPED\x10\x01\x12\x11\n\rRAPID_RUNNING\x10\x02\"!\n\x0e\x45gmTestSignals\x12\x0f\n\x07signals\x18\x01 \x03(\x01\"3\n\x10\x45gmMeasuredForce\x12\x10\n\x08\x66\x63\x41\x63tive\x18\x01 \x01(\x08\x12\r\n\x05\x66orce\x18\x02 \x03(\x01\"C\n\x10\x45gmCollisionInfo\x12\x19\n\x11\x63ollsionTriggered\x18\x01 \x01(\x08\x12\x14\n\x0c\x63ollDetQuota\x18\x02 \x03(\x01\",\n\x0c\x45gmRAPIDdata\x12\x0e\n\x06\x64igVal\x18\x01 \x01(\x08\x12\x0c\n\x04\x64num\x18\x02 \x03(\x01\"\x90\x04\n\x08\x45gmRobot\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmHeader\x12&\n\x08\x66\x65\x65\x64\x42\x61\x63k\x18\x02 \x01(\x0b\x32\x14.abb.egm.EgmFeedBack\x12$\n\x07planned\x18\x03 \x01(\x0b\x32\x13.abb.egm.EgmPlanned\x12*\n\nmotorState\x18\x04 \x01(\x0b\x32\x16.abb.egm.EgmMotorState\x12&\n\x08mciState\x18\x05 \x01(\x0b\x32\x14.abb.egm.EgmMCIState\x12\x19\n\x11mciConvergenceMet\x18\x06 \x01(\x08\x12,\n\x0btestSignals\x18\x07 \x01(\x0b\x32\x17.abb.egm.EgmTestSignals\x12\x36\n\x0erapidExecState\x18\x08 \x01(\x0b\x32\x1e.abb.egm.EgmRapidCtrlExecState\x12\x30\n\rmeasuredForce\x18\t \x01(\x0b\x32\x19.abb.egm.EgmMeasuredForce\x12\x17\n\x0futilizationRate\x18\n \x01(\x01\x12\x11\n\tmoveIndex\x18\x0b \x01(\r\x12\x30\n\rCollisionInfo\x18\x0c \x01(\x0b\x32\x19.abb.egm.EgmCollisionInfo\x12-\n\x0eRAPIDfromRobot\x18\r \x01(\x0b\x32\x15.abb.egm.EgmRAPIDdata\"\xaa\x01\n\tEgmSensor\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmHeader\x12$\n\x07planned\x18\x02 \x01(\x0b\x32\x13.abb.egm.EgmPlanned\x12&\n\x08speedRef\x18\x03 \x01(\x0b\x32\x14.abb.egm.EgmSpeedRef\x12+\n\x0cRAPIDtoRobot\x18\x04 \x01(\x0b\x32\x15.abb.egm.EgmRAPIDdata\"_\n\x11\x45gmSensorPathCorr\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmHeader\x12&\n\x08pathCorr\x18\x02 \x01(\x0b\x32\x14.abb.egm.EgmPathCorr')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'egm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EGMHEADER']._serialized_start=23
  _globals['_EGMHEADER']._serialized_end=258
  _globals['_EGMHEADER_MESSAGETYPE']._serialized_start=130
  _globals['_EGMHEADER_MESSAGETYPE']._serialized_end=258
  _globals['_EGMCARTESIAN']._serialized_start=260
  _globals['_EGMCARTESIAN']._serialized_end=307
  _globals['_EGMQUATERNION']._serialized_start=309
  _globals['_EGMQUATERNION']._serialized_end=372
  _globals['_EGMEULER']._serialized_start=374
  _globals['_EGMEULER']._serialized_end=417
  _globals['_EGMCLOCK']._serialized_start=419
  _globals['_EGMCLOCK']._serialized_end=456
  _globals['_EGMPOSE']._serialized_start=458
  _globals['_EGMPOSE']._serialized_end=577
  _globals['_EGMCARTESIANSPEED']._serialized_start=579
  _globals['_EGMCARTESIANSPEED']._serialized_end=613
  _globals['_EGMJOINTS']._serialized_start=615
  _globals['_EGMJOINTS']._serialized_end=642
  _globals['_EGMEXTERNALJOINTS']._serialized_start=644
  _globals['_EGMEXTERNALJOINTS']._serialized_end=679
  _globals['_EGMPLANNED']._serialized_start=682
  _globals['_EGMPLANNED']._serialized_end=844
  _globals['_EGMSPEEDREF']._serialized_start=847
  _globals['_EGMSPEEDREF']._serialized_end=988
  _globals['_EGMPATHCORR']._serialized_start=990
  _globals['_EGMPATHCORR']._serialized_end=1052
  _globals['_EGMFEEDBACK']._serialized_start=1055
  _globals['_EGMFEEDBACK']._serialized_end=1218
  _globals['_EGMMOTORSTATE']._serialized_start=1221
  _globals['_EGMMOTORSTATE']._serialized_end=1361
  _globals['_EGMMOTORSTATE_MOTORSTATETYPE']._serialized_start=1292
  _globals['_EGMMOTORSTATE_MOTORSTATETYPE']._serialized_end=1361
  _globals['_EGMMCISTATE']._serialized_start=1364
  _globals['_EGMMCISTATE']._serialized_end=1526
  _globals['_EGMMCISTATE_MCISTATETYPE']._serialized_start=1444
  _globals['_EGMMCISTATE_MCISTATETYPE']._serialized_end=1526
  _globals['_EGMRAPIDCTRLEXECSTATE']._serialized_start=1529
  _globals['_EGMRAPIDCTRLEXECSTATE']._serialized_end=1724
  _globals['_EGMRAPIDCTRLEXECSTATE_RAPIDCTRLEXECSTATETYPE']._serialized_start=1641
  _globals['_EGMRAPIDCTRLEXECSTATE_RAPIDCTRLEXECSTATETYPE']._serialized_end=1724
  _globals['_EGMTESTSIGNALS']._serialized_start=1726
  _globals['_EGMTESTSIGNALS']._serialized_end=1759
  _globals['_EGMMEASUREDFORCE']._serialized_start=1761
  _globals['_EGMMEASUREDFORCE']._serialized_end=1812
  _globals['_EGMCOLLISIONINFO']._serialized_start=1814
  _globals['_EGMCOLLISIONINFO']._serialized_end=1881
  _globals['_EGMRAPIDDATA']._serialized_start=1883
  _globals['_EGMRAPIDDATA']._serialized_end=1927
  _globals['_EGMROBOT']._serialized_start=1930
  _globals['_EGMROBOT']._serialized_end=2458
  _globals['_EGMSENSOR']._serialized_start=2461
  _globals['_EGMSENSOR']._serialized_end=2631
  _globals['_EGMSENSORPATHCORR']._serialized_start=2633
  _globals['_EGMSENSORPATHCORR']._serialized_end=2728
# @@protoc_insertion_point(module_scope)
