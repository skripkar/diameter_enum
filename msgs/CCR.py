#       CCR.py
#       
#       Copyright 2017 Daniel Mende <mail@c0decafe.de>
#

#       Redistribution and use in source and binary forms, with or without
#       modification, are permitted provided that the following conditions are
#       met:
#       
#       * Redistributions of source code must retain the above copyright
#         notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above
#         copyright notice, this list of conditions and the following disclaimer
#         in the documentation and/or other materials provided with the
#         distribution.
#       * Neither the name of the  nor the names of its
#         contributors may be used to endorse or promote products derived from
#         this software without specific prior written permission.
#       
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#       AS IS AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from libDiameter import *
from message import Message

#RFC4006 - 3.1

#~ <Credit-Control-Request> ::= < Diameter Header: 272, REQ, PXY >
                                   #~ < Session-Id >
                                   #~ { Origin-Host }
                                   #~ { Origin-Realm }
                                   #~ { Destination-Realm }
                                   #~ { Auth-Application-Id }
                                   #~ { Service-Context-Id }
                                   #~ { CC-Request-Type }
                                   #~ { CC-Request-Number }
                                   #~ [ Destination-Host ]
                                   #~ [ User-Name ]
                                   #~ [ CC-Sub-Session-Id ]
                                   #~ [ Acct-Multi-Session-Id ]
                                   #~ [ Origin-State-Id ]
                                   #~ [ Event-Timestamp ]
                                  #~ *[ Subscription-Id ]
                                   #~ [ Service-Identifier ]
                                   #~ [ Termination-Cause ]
                                   #~ [ Requested-Service-Unit ]
                                   #~ [ Requested-Action ]
                                  #~ *[ Used-Service-Unit ]
                                   #~ [ Multiple-Services-Indicator ]
                                  #~ *[ Multiple-Services-Credit-Control ]
                                  #~ *[ Service-Parameter-Info ]
                                   #~ [ CC-Correlation-Id ]
                                   #~ [ User-Equipment-Info ]
                                  #~ *[ Proxy-Info ]
                                  #~ *[ Route-Record ]
                                  #~ *[ AVP ]

def create_pkg(config):
    return Message(4, "Credit-Control",
        [DIAMETER_HDR_PROXIABLE, DIAMETER_HDR_REQUEST], [
            ("Session-Id", config["session-id"]),
            ("Origin-Host", config["origin-host"]),
            ("Origin-Realm", config["origin-realm"]),
            ("Destination-Host", config["destination-host"]),
            ("Destination-Realm", config["destination-realm"]),
            ("Auth-Application-Id", dictCOMMANDname2code("Re-Auth")),
        ])
