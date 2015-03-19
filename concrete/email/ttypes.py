#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class EmailAddress(object):
  """
  An email address, optionally accompanied by a display_name. These
  values are typically extracted from strings such as:
  <tt> "John Smith" &lt;john\@xyz.com&gt; </tt>.

  \see RFC2822 <http://tools.ietf.org/html/rfc2822>

  Attributes:
   - address
   - displayName
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'address', None, None, ), # 1
    (2, TType.STRING, 'displayName', None, None, ), # 2
  )

  def __init__(self, address=None, displayName=None,):
    self.address = address
    self.displayName = displayName

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.address = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.displayName = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EmailAddress')
    if self.address is not None:
      oprot.writeFieldBegin('address', TType.STRING, 1)
      oprot.writeString(self.address.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.displayName is not None:
      oprot.writeFieldBegin('displayName', TType.STRING, 2)
      oprot.writeString(self.displayName.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.address)
    value = (value * 31) ^ hash(self.displayName)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EmailCommunicationInfo(object):
  """
  Extra information about an email communication instance.

  Attributes:
   - messageId
   - contentType
   - userAgent
   - inReplyToList
   - referenceList
   - senderAddress
   - returnPathAddress
   - toAddressList
   - ccAddressList
   - bccAddressList
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'messageId', None, None, ), # 1
    (2, TType.STRING, 'contentType', None, None, ), # 2
    (3, TType.STRING, 'userAgent', None, None, ), # 3
    (4, TType.LIST, 'inReplyToList', (TType.STRING,None), None, ), # 4
    (5, TType.LIST, 'referenceList', (TType.STRING,None), None, ), # 5
    (6, TType.STRUCT, 'senderAddress', (EmailAddress, EmailAddress.thrift_spec), None, ), # 6
    (7, TType.STRUCT, 'returnPathAddress', (EmailAddress, EmailAddress.thrift_spec), None, ), # 7
    (8, TType.LIST, 'toAddressList', (TType.STRUCT,(EmailAddress, EmailAddress.thrift_spec)), None, ), # 8
    (9, TType.LIST, 'ccAddressList', (TType.STRUCT,(EmailAddress, EmailAddress.thrift_spec)), None, ), # 9
    (10, TType.LIST, 'bccAddressList', (TType.STRUCT,(EmailAddress, EmailAddress.thrift_spec)), None, ), # 10
  )

  def __init__(self, messageId=None, contentType=None, userAgent=None, inReplyToList=None, referenceList=None, senderAddress=None, returnPathAddress=None, toAddressList=None, ccAddressList=None, bccAddressList=None,):
    self.messageId = messageId
    self.contentType = contentType
    self.userAgent = userAgent
    self.inReplyToList = inReplyToList
    self.referenceList = referenceList
    self.senderAddress = senderAddress
    self.returnPathAddress = returnPathAddress
    self.toAddressList = toAddressList
    self.ccAddressList = ccAddressList
    self.bccAddressList = bccAddressList

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.messageId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.contentType = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.userAgent = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.inReplyToList = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString().decode('utf-8')
            self.inReplyToList.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.referenceList = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readString().decode('utf-8')
            self.referenceList.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRUCT:
          self.senderAddress = EmailAddress()
          self.senderAddress.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRUCT:
          self.returnPathAddress = EmailAddress()
          self.returnPathAddress.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.toAddressList = []
          (_etype15, _size12) = iprot.readListBegin()
          for _i16 in xrange(_size12):
            _elem17 = EmailAddress()
            _elem17.read(iprot)
            self.toAddressList.append(_elem17)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.LIST:
          self.ccAddressList = []
          (_etype21, _size18) = iprot.readListBegin()
          for _i22 in xrange(_size18):
            _elem23 = EmailAddress()
            _elem23.read(iprot)
            self.ccAddressList.append(_elem23)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.LIST:
          self.bccAddressList = []
          (_etype27, _size24) = iprot.readListBegin()
          for _i28 in xrange(_size24):
            _elem29 = EmailAddress()
            _elem29.read(iprot)
            self.bccAddressList.append(_elem29)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EmailCommunicationInfo')
    if self.messageId is not None:
      oprot.writeFieldBegin('messageId', TType.STRING, 1)
      oprot.writeString(self.messageId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.contentType is not None:
      oprot.writeFieldBegin('contentType', TType.STRING, 2)
      oprot.writeString(self.contentType.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.userAgent is not None:
      oprot.writeFieldBegin('userAgent', TType.STRING, 3)
      oprot.writeString(self.userAgent.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.inReplyToList is not None:
      oprot.writeFieldBegin('inReplyToList', TType.LIST, 4)
      oprot.writeListBegin(TType.STRING, len(self.inReplyToList))
      for iter30 in self.inReplyToList:
        oprot.writeString(iter30.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.referenceList is not None:
      oprot.writeFieldBegin('referenceList', TType.LIST, 5)
      oprot.writeListBegin(TType.STRING, len(self.referenceList))
      for iter31 in self.referenceList:
        oprot.writeString(iter31.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.senderAddress is not None:
      oprot.writeFieldBegin('senderAddress', TType.STRUCT, 6)
      self.senderAddress.write(oprot)
      oprot.writeFieldEnd()
    if self.returnPathAddress is not None:
      oprot.writeFieldBegin('returnPathAddress', TType.STRUCT, 7)
      self.returnPathAddress.write(oprot)
      oprot.writeFieldEnd()
    if self.toAddressList is not None:
      oprot.writeFieldBegin('toAddressList', TType.LIST, 8)
      oprot.writeListBegin(TType.STRUCT, len(self.toAddressList))
      for iter32 in self.toAddressList:
        iter32.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.ccAddressList is not None:
      oprot.writeFieldBegin('ccAddressList', TType.LIST, 9)
      oprot.writeListBegin(TType.STRUCT, len(self.ccAddressList))
      for iter33 in self.ccAddressList:
        iter33.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.bccAddressList is not None:
      oprot.writeFieldBegin('bccAddressList', TType.LIST, 10)
      oprot.writeListBegin(TType.STRUCT, len(self.bccAddressList))
      for iter34 in self.bccAddressList:
        iter34.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.messageId)
    value = (value * 31) ^ hash(self.contentType)
    value = (value * 31) ^ hash(self.userAgent)
    value = (value * 31) ^ hash(self.inReplyToList)
    value = (value * 31) ^ hash(self.referenceList)
    value = (value * 31) ^ hash(self.senderAddress)
    value = (value * 31) ^ hash(self.returnPathAddress)
    value = (value * 31) ^ hash(self.toAddressList)
    value = (value * 31) ^ hash(self.ccAddressList)
    value = (value * 31) ^ hash(self.bccAddressList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)