#!/usr/bin/env python

# This script converts between Thrift protocol embeddings.
# Usage is:
# python convert_protocols.py \
#   --input-file /path/to/input/file
#   --output-file /path/to/output/file
#   --direction <known conversion>
#
# <known conversion> is a categorical directive, in the form
#   <input-encoding>-to-<output-encoding>
# The --input-file must be in the input format; the output file will
# be in the <output-encoding>
#
# <known conversion> must currently be either
#   * binary-to-compact: Convert the TBinaryProtocol encoded input file to a TCompactProtocol encoded output file
#   * compact-to-binary: Convert the TCompactProtocol encoded input file to a TBinaryProtocol encoded output file
#
# The known conversions are stored in a dictionary KNOWN_CONVERSIONS:
#   * keys are the conversion name, e.g., 'binary-to-compact'
#   * values are pairs of callable factory methods (callable-input-factory, callable-output-factory), e.g.,
#        (TBinaryProtocol.TBinaryProtocolFactory, TCompactProtocol.TCompactProtocolFactory)
#
# Therefore, adding to the conversions is simple: just add to the KNOWN_CONVERSIONS mapping.

import argparse
import gzip
from thrift import TSerialization
from thrift.protocol import TCompactProtocol, TBinaryProtocol
from thrift.transport import TTransport
from concrete import Communication
import mimetypes

KNOWN_CONVERSIONS = {
    'binary-to-compact':(TBinaryProtocol.TBinaryProtocolFactory, TCompactProtocol.TCompactProtocolFactory),
    'compact-to-binary':(TCompactProtocol.TCompactProtocolFactory, TBinaryProtocol.TBinaryProtocolFactory)
}

def make_parser():
    parser = argparse.ArgumentParser(description='Convert communications between protocols')
    parser.add_argument('--input-file', type=str, required=True,
                        help='input file path')
    parser.add_argument('--output-file', type=str, required=True,
                        help='output file path')
    parser.add_argument('--direction', choices = KNOWN_CONVERSIONS.keys(), required=True)
    return parser

def convert(input_file_path, output_file_path, input_protocol_factory, output_protocol_factory):
    """
    Convert an input file (to be read in as an input_protocol_factory type)
    to an output file (with encoding output_protocol_factory type).
    
    * input_file_path: Path to the input file (on disk)
    * output_file_path: Path the output file (on disk)
    * input_protocol_factory: Callable factory function for input encoding, e.g., TBinaryProtocol.TBinaryProtocolFactory.
    * output_protocol_factory: Callable factory function for output encoding, e.g., TCompactProtocol.TCompactProtocolFactory.
    """
    input_file = open(input_file_path,'r')
    input_bytes = input_file.read()
    output_bytes = convert_communication(input_bytes, input_protocol_factory, output_protocol_factory)
    input_file.close()
    output_file = open(output_file_path,'w')
    output_file.write(output_bytes)
    output_file.close()

def convert_communication(input_bytes, input_protocol_factory, output_protocol_factory):
    """
    Convert an input byte stream (to be read in as an input_protocol_factory type)
    to an output byte stream (with encoding output_protocol_factory type).
    
    * input_bytes: Input file byte stream
    * input_protocol_factory: Callable factory function for input encoding, e.g., TBinaryProtocol.TBinaryProtocolFactory.
    * output_protocol_factory: Callable factory function for output encoding, e.g., TCompactProtocol.TCompactProtocolFactory.
    """
    comm = Communication()
    TSerialization.deserialize(comm, input_bytes, protocol_factory = KNOWN_CONVERSIONS[args.direction][0]())
    output_bytes = TSerialization.serialize(comm, protocol_factory = KNOWN_CONVERSIONS[args.direction][1]())
    return output_bytes
    
if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    mimetypes.init()
    (ifile_type, ifile_encoding) = mimetypes.guess_type(args.input_file)
    (ofile_type, ofile_encoding) = mimetypes.guess_type(args.output_file)
    out_writer = None
    if ofile_encoding == "gzip":
        out_writer = gzip.GzipFile(args.output_file, 'wb')
    else:
        out_writer = open(args.output_file, 'w')
    if ifile_encoding == 'gzip':
        f = gzip.GzipFile(args.input_file)
        transportIn = TTransport.TFileObjectTransport(f)
        protocolIn = KNOWN_CONVERSIONS[args.direction][0]().getProtocol(transportIn)
        while True:
            try:
                comm = Communication()
                comm.read(protocolIn)
                output_bytes = TSerialization.serialize(comm, protocol_factory = KNOWN_CONVERSIONS[args.direction][1]())
                out_writer.write(output_bytes)
            except EOFError:
                break
        f.close()
    else:
        convert(input_file_path  = args.input_file,
                output_file_path = args.output_file,
                input_protocol_factory  = KNOWN_CONVERSIONS[args.direction][0],
                output_protocol_factory = KNOWN_CONVERSIONS[args.direction][1])
    out_writer.close()
