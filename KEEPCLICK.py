import pandas as pd
import streamlit as st
import time
from streamlit import components
import io
import json
import json

import web3
from web3 import Web3
import requests
from time import sleep
import subprocess
from json.decoder import JSONDecodeError


st.title('KEEP ECDSA+BEACON')

st.markdown(("""
       <!DOCTYPE html>
<style>
html {
  background: #f3ffe6;
  font-family: helvetica;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: red;

  .blue {
    color: #53d9d1;
  }
  .pink {
    color: white;
  }
  .orange {
    color: #eb7132;
  }
  .console {
    border: 1px solid #333;
    border-radius: 3px;
    margin: 2rem;

    box-shadow: 0 0 15px 0px rgba(0, 0, 0, 0.75);
    .top {
      background: #333;
      color: blue;
      text-align: center;
      font-size: 12px;
      padding: 5px;
      .options {
        font-size: 16px;
        float: left;
      }
    }
    .text {
      font-family: courier;
      color: blue;
      font-size: 14px;
      padding: 0.25rem;
    }
  }
}

.typewriter {
  overflow: hidden;
  width: fit-content;
  white-space: nowrap;
  border-right: 0.10em solid #eb7132;
  animation: typing 1s steps(15, end), blink-caret 0.75s step-end infinite;
}
.stTextInput>div>div>input {
    color: #4F8BF9;
}

/* The typing effect */
@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 60%;
  }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
  from,
  to {
    border-color: transparent;
  }
  50% {
    border-color: orange;
  }
}
/* Google Fonts */
@import url(https://fonts.googleapis.com/css?family=Anonymous+Pro);

/* Global */
html{
  min-height: 100%;
  overflow: hidden;
}

.line-1{
    position: relative;
    top: 50%;  
    width: 24em;
    margin: 0 auto;
    border-right: 2px solid rgba(255,255,255,.75);
    font-size: 180%;
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    transform: translateY(-50%);    
}

/* Animation */
.anim-typewriter{
  animation: typewriter 4s steps(44 , end) 1s 1 normal both,
             blinkTextCursor 500ms steps(44) infinite normal;
}
@keyframes typewriter{
  from{width: 0;}
  to{width: 25em;}
}
@keyframes blinkTextCursor{
  from{border-right-color: rgba(255,255,255,.75);}
  to{border-right-color: green;}
}
@import url(https://fonts.googleapis.com/css?family=Khula:700);
body {
  background: lightgreen;
}
.hidden {
  opacity:0;
}
.console-container {

  font-family:Khula;
  font-size:4em;
  text-align:center;
  height:200px;
  width:600px;
  display:block;
  position:absolute;
  color:white;
  top:0;
  bottom:0;
  left:0;
  right:0;
  margin:auto;
}
.console-underscore {
   display:inline-block;
  position:relative;
  top:-0.14em;
  left:10px;
}
</style>

<div><p class="line-1 anim-typewriter">KEEP NODE without linux terminal for 1 click :)</p><div>
<div class="console">
  <div class="top"> <span class="options">⦿ ○ ○</span> <span class="title">KEEP ECDSA/BEACON </span></div>
  <div class="tabs"> </div>
  <div class="text">
    <br>[06:24:55] Finished FREE geth Node <span class="pink">'warm-up-hands'</span> after 0.00 s
    <br>[06:24:55] Starting secure<span class="pink">'No DB + Secure '</span>...
    <br> [06:25:14] KEEP_bin <span class="blue">234</span> steps, <span class="blue">234</span> passes, <span class="blue">0</span> failures: <span class="pink">'<font color=‘black’>SUCCESS</font>'</span>
    <br>
    <p class="typewriter"> root@KEEP sudo <span class="pink">  docker run -d</span></p>
    </span>
  </div>
</div>


</html>
<!-- TradingView Widget END -->
        """), unsafe_allow_html=True)
# st.write(first_name)
st.markdown('<font color=‘black’>To continue, you need to create a MEW and VPS</font>', unsafe_allow_html=True)

ropsten_url = "http://135.181.59.188:8545"
web3 = Web3(Web3.HTTPProvider(ropsten_url))

st.set_option('deprecation.showfileUploaderEncoding', False)
# file_buffer = st.file_uploader(...)

# text_io = io.TextIOWrapper(file_buffer)
web3 = Web3(Web3.HTTPProvider(ropsten_url))

abi=[{'inputs': [{'internalType': 'contract ERC20Burnable',
    'name': '_token',
    'type': 'address'},
   {'internalType': 'contract TokenGrant',
    'name': '_tokenGrant',
    'type': 'address'},
   {'internalType': 'contract TokenStakingEscrow',
    'name': '_escrow',
    'type': 'address'},
   {'internalType': 'contract KeepRegistry',
    'name': '_registry',
    'type': 'address'},
   {'internalType': 'uint256',
    'name': '_initializationPeriod',
    'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'constructor'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'lockCreator',
    'type': 'address'}],
  'name': 'ExpiredLockReleased',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'lockCreator',
    'type': 'address'}],
  'name': 'LockReleased',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'beneficiary',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'authorizer',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'value',
    'type': 'uint256'}],
  'name': 'OperatorStaked',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': False,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'}],
  'name': 'RecoveredStake',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'owner',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'}],
  'name': 'StakeDelegated',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'lockCreator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'until',
    'type': 'uint256'}],
  'name': 'StakeLocked',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'newOwner',
    'type': 'address'}],
  'name': 'StakeOwnershipTransferred',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'}],
  'name': 'TokensSeized',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'}],
  'name': 'TokensSlashed',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'newAmount',
    'type': 'uint256'}],
  'name': 'TopUpCompleted',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'topUp',
    'type': 'uint256'}],
  'name': 'TopUpInitiated',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'undelegatedAt',
    'type': 'uint256'}],
  'name': 'Undelegated',
  'type': 'event'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address',
    'name': '_operatorContract',
    'type': 'address'}],
  'name': 'activeStake',
  'outputs': [{'internalType': 'uint256',
    'name': 'balance',
    'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address',
    'name': '_operatorContract',
    'type': 'address'}],
  'name': 'authorizeOperatorContract',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'authorizerOf',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_address',
    'type': 'address'}],
  'name': 'balanceOf',
  'outputs': [{'internalType': 'uint256',
    'name': 'balance',
    'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'beneficiaryOf',
  'outputs': [{'internalType': 'address payable',
    'name': '',
    'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'cancelStake',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'delegatedAuthoritySource',
    'type': 'address'}],
  'name': 'claimDelegatedAuthority',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'commitTopUp',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'deployedAt',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address',
    'name': '_operatorContract',
    'type': 'address'}],
  'name': 'eligibleStake',
  'outputs': [{'internalType': 'uint256',
    'name': 'balance',
    'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': 'operatorContract',
    'type': 'address'}],
  'name': 'getAuthoritySource',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'getDelegationInfo',
  'outputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'createdAt', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'undelegatedAt', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'}],
  'name': 'getLocks',
  'outputs': [{'internalType': 'address[]',
    'name': 'creators',
    'type': 'address[]'},
   {'internalType': 'uint256[]', 'name': 'expirations', 'type': 'uint256[]'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': 'staker', 'type': 'address'},
   {'internalType': 'address', 'name': 'operatorContract', 'type': 'address'}],
  'name': 'hasMinimumStake',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'initializationPeriod',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operatorContract',
    'type': 'address'}],
  'name': 'isApprovedOperatorContract',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address',
    'name': '_operatorContract',
    'type': 'address'}],
  'name': 'isAuthorizedForOperator',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'}],
  'name': 'isStakeLocked',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'uint256', 'name': 'duration', 'type': 'uint256'}],
  'name': 'lockStake',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'minimumStake',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'ownerOf',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address', 'name': '_from', 'type': 'address'},
   {'internalType': 'uint256', 'name': '_value', 'type': 'uint256'},
   {'internalType': 'address', 'name': '_token', 'type': 'address'},
   {'internalType': 'bytes', 'name': '_extraData', 'type': 'bytes'}],
  'name': 'receiveApproval',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'recoverStake',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'address', 'name': 'operatorContract', 'type': 'address'}],
  'name': 'releaseExpiredLock',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': 'amountToSeize',
    'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'rewardMultiplier', 'type': 'uint256'},
   {'internalType': 'address', 'name': 'tattletale', 'type': 'address'},
   {'internalType': 'address[]',
    'name': 'misbehavedOperators',
    'type': 'address[]'}],
  'name': 'seize',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': 'amountToSlash',
    'type': 'uint256'},
   {'internalType': 'address[]',
    'name': 'misbehavedOperators',
    'type': 'address[]'}],
  'name': 'slash',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'address', 'name': 'newOwner', 'type': 'address'}],
  'name': 'transferStakeOwnership',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'undelegate',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'uint256',
    'name': '_undelegationTimestamp',
    'type': 'uint256'}],
  'name': 'undelegateAt',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'undelegationPeriod',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'}],
  'name': 'unlockStake',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'}]

address_1 = web3.toChecksumAddress("0x234d2182B29c6a64ce3ab6940037b5C8FdAB608e")

TokenStaking = web3.eth.contract(address=address_1, abi=abi)

# TokenGrant
abi=[{'inputs': [{'internalType': 'address',
    'name': '_serviceContract',
    'type': 'address'},
   {'internalType': 'address', 'name': '_tokenStaking', 'type': 'address'},
   {'internalType': 'address', 'name': '_keepRegistry', 'type': 'address'},
   {'internalType': 'address', 'name': '_gasPriceOracle', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'constructor'},
 {'anonymous': False,
  'inputs': [{'indexed': False,
    'internalType': 'uint256',
    'name': 'memberIndex',
    'type': 'uint256'},
   {'indexed': False,
    'internalType': 'bytes',
    'name': 'groupPubKey',
    'type': 'bytes'},
   {'indexed': False,
    'internalType': 'bytes',
    'name': 'misbehaved',
    'type': 'bytes'}],
  'name': 'DkgResultSubmittedEvent',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'beneficiary',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'groupIndex',
    'type': 'uint256'}],
  'name': 'GroupMemberRewardsWithdrawn',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': False,
    'internalType': 'uint256',
    'name': 'newEntry',
    'type': 'uint256'}],
  'name': 'GroupSelectionStarted',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': False,
    'internalType': 'bytes',
    'name': 'groupPubKey',
    'type': 'bytes'}],
  'name': 'OnGroupRegistered',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': False,
    'internalType': 'bytes',
    'name': 'previousEntry',
    'type': 'bytes'},
   {'indexed': False,
    'internalType': 'bytes',
    'name': 'groupPublicKey',
    'type': 'bytes'}],
  'name': 'RelayEntryRequested',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [],
  'name': 'RelayEntrySubmitted',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'uint256',
    'name': 'groupIndex',
    'type': 'uint256'}],
  'name': 'RelayEntryTimeoutReported',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'uint256',
    'name': 'groupIndex',
    'type': 'uint256'}],
  'name': 'UnauthorizedSigningReported',
  'type': 'event'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'serviceContract',
    'type': 'address'}],
  'name': 'addServiceContract',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': '_newEntry',
    'type': 'uint256'},
   {'internalType': 'address payable',
    'name': 'submitter',
    'type': 'address'}],
  'name': 'createGroup',
  'outputs': [],
  'payable': True,
  'stateMutability': 'payable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'currentRequestGroupIndex',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'currentRequestPreviousEntry',
  'outputs': [{'internalType': 'bytes', 'name': '', 'type': 'bytes'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'currentRequestStartBlock',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'dkgGasEstimate',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'dkgSubmitterReimbursementFee',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'entryVerificationFee',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'entryVerificationGasEstimate',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'gasPriceCeiling',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [],
  'name': 'genesis',
  'outputs': [],
  'payable': True,
  'stateMutability': 'payable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'getFirstActiveGroupIndex',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'bytes',
    'name': 'groupPubKey',
    'type': 'bytes'}],
  'name': 'getGroupMemberRewards',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'bytes',
    'name': 'groupPubKey',
    'type': 'bytes'}],
  'name': 'getGroupMembers',
  'outputs': [{'internalType': 'address[]',
    'name': 'members',
    'type': 'address[]'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256',
    'name': 'groupIndex',
    'type': 'uint256'}],
  'name': 'getGroupPublicKey',
  'outputs': [{'internalType': 'bytes', 'name': '', 'type': 'bytes'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256',
    'name': 'groupIndex',
    'type': 'uint256'}],
  'name': 'getGroupRegistrationTime',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'getNumberOfCreatedGroups',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'groupCreationFee',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'groupMemberBaseReward',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'groupProfitFee',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'groupSelectionGasEstimate',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'groupSize',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'groupThreshold',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': 'staker', 'type': 'address'}],
  'name': 'hasMinimumStake',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'uint256', 'name': 'groupIndex', 'type': 'uint256'}],
  'name': 'hasWithdrawnRewards',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'isEntryInProgress',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'bytes',
    'name': 'groupPubKey',
    'type': 'bytes'}],
  'name': 'isGroupRegistered',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'isGroupSelectionPossible',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256',
    'name': 'groupIndex',
    'type': 'uint256'}],
  'name': 'isGroupTerminated',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'bytes',
    'name': 'groupPubKey',
    'type': 'bytes'}],
  'name': 'isStaleGroup',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'numberOfGroups',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [],
  'name': 'refreshGasPrice',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'bytes',
    'name': '_groupSignature',
    'type': 'bytes'}],
  'name': 'relayEntry',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'relayEntryTimeout',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [],
  'name': 'reportRelayEntryTimeout',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': 'groupIndex',
    'type': 'uint256'},
   {'internalType': 'bytes', 'name': 'signedMsgSender', 'type': 'bytes'}],
  'name': 'reportUnauthorizedSigning',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'resultPublicationBlockStep',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'selectedParticipants',
  'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': 'requestId',
    'type': 'uint256'},
   {'internalType': 'bytes', 'name': 'previousEntry', 'type': 'bytes'}],
  'name': 'sign',
  'outputs': [],
  'payable': True,
  'stateMutability': 'payable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': 'submitterMemberIndex',
    'type': 'uint256'},
   {'internalType': 'bytes', 'name': 'groupPubKey', 'type': 'bytes'},
   {'internalType': 'bytes', 'name': 'misbehaved', 'type': 'bytes'},
   {'internalType': 'bytes', 'name': 'signatures', 'type': 'bytes'},
   {'internalType': 'uint256[]',
    'name': 'signingMembersIndexes',
    'type': 'uint256[]'}],
  'name': 'submitDkgResult',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'bytes32', 'name': 'ticket', 'type': 'bytes32'}],
  'name': 'submitTicket',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'submittedTickets',
  'outputs': [{'internalType': 'uint64[]', 'name': '', 'type': 'uint64[]'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'ticketSubmissionTimeout',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'uint256', 'name': 'groupIndex', 'type': 'uint256'}],
  'name': 'withdrawGroupMemberRewards',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'}]
address = web3.toChecksumAddress("0xC8337a94a50d16191513dEF4D1e61A6886BF410f")
# bytecode = "0x60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032"
# bytecode = "0x60806040526000805460ff191690553480156200001b57600080fd5b506200003463deadbeef6001600160e01b036200003a16565b620000f4565b6001600160a01b038116620000815760405162461bcd60e51b8152600401808060200182810382526023815260200180620032ed6023913960400191505060405180910390fd5b60005460ff1615620000c55760405162461bcd60e51b8152600401808060200182810382526025815260200180620033106025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b6131e980620001046000396000f3fe60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e"
# bytecode = "0x610793610026600b82828239805160001a60731461001957fe5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600436106101ce5760003560e01c80639df1b34611610103578063c28eab40116100a1578063e0dfa4b31161007b578063e0dfa4b314610523578063ef2bd3d014610540578063f09911ee1461055d578063fb0611ff14610587576101ce565b8063c28eab40146104bf578063cb4536ad146104e9578063dcf5c88c14610506576101ce565b8063afb8e293116100dd578063afb8e2931461044b578063b0b6855a14610468578063b5e6a0a014610485578063b65fb6cb146104a2576101ce565b80639df1b346146103e7578063a2f9a98014610404578063a6fd0b5614610421576101ce565b806348312fa311610170578063652d34301161014a578063652d3430146103595780636fdbb3c414610376578063761275bf146103a05780638be5e97f146103bd576101ce565b806348312fa3146102f55780635a332575146103125780635dd33d991461032f576101ce565b8063171b2a05116101ac578063171b2a051461025a57806327f2744914610284578063375ec420146102a1578063429fcb0d146102cb576101ce565b8063056256a8146101d35780630f2c6355146101ff57806316cddf4e14610230575b600080fd5b8180156101df57600080fd5b506101fd600480360360208110156101f657600080fd5b50356105a4565b005b61021c6004803603602081101561021557600080fd5b50356105c6565b604080519115158252519081900360200190f35b81801561023c57600080fd5b506101fd6004803603602081101561025357600080fd5b50356105e6565b81801561026657600080fd5b506101fd6004803603602081101561027d57600080fd5b50356105ed565b61021c6004803603602081101561029a57600080fd5b50356105f4565b8180156102ad57600080fd5b506101fd600480360360208110156102c457600080fd5b50356105fd565b8180156102d757600080fd5b506101fd600480360360208110156102ee57600080fd5b5035610604565b61021c6004803603602081101561030b57600080fd5b503561060b565b61021c6004803603602081101561032857600080fd5b5035610634565b81801561033b57600080fd5b506101fd6004803603602081101561035257600080fd5b5035610671565b61021c6004803603602081101561036f57600080fd5b5035610678565b81801561038257600080fd5b506101fd6004803603602081101561039957600080fd5b5035610680565b61021c600480360360208110156103b657600080fd5b5035610687565b8180156103c957600080fd5b506101fd600480360360208110156103e057600080fd5b5035610690565b61021c600480360360208110156103fd57600080fd5b5035610697565b61021c6004803603602081101561041a57600080fd5b50356106a0565b81801561042d57600080fd5b506101fd6004803603602081101561044457600080fd5b50356106a9565b61021c6004803603602081101561046157600080fd5b50356106b0565b61021c6004803603602081101561047e57600080fd5b50356106d4565b61021c6004803603602081101561049b57600080fd5b50356106dd565b61021c600480360360208110156104b857600080fd5b50356106e6565b8180156104cb57600080fd5b506101fd600480360360208110156104e257600080fd5b50356106ef565b61021c600480360360208110156104ff57600080fd5b50356106f6565b61021c6004803603602081101561051c57600080fd5b50356106ff565b61021c6004803603602081101561053957600080fd5b5035610708565b61021c6004803603602081101561055657600080fd5b503561072b565b81801561056957600080fd5b506101fd6004803603602081101561058057600080fd5b5035610734565b61021c6004803603602081101561059d57600080fd5b503561073b565b600b5b81600401601c6101000a81548160ff021916908360ff16021790555050565b600060045b6004830154600160e01b900460ff9081169116149050919050565b60016105a7565b60086105a7565b600060026105cb565b60046105a7565b60056105a7565b600481015460009060ff600160e01b909104166001148061062e575060026105cb565b92915050565b600481015460009060ff600160e01b90910416600b14806106645750600482015460ff600160e01b909104166007145b8061062e575060036105cb565b600a6105a7565b6000806105cb565b60036105a7565b600060086105cb565b60026105a7565b6000600b6105cb565b600060096105cb565b60066105a7565b6000600480830154600160e01b900460ff9081169116148061062e575060086105cb565b600060076105cb565b600060016105cb565b600060036105cb565b60096105a7565b600060066105cb565b6000600a6105cb565b600481015460009060ff600160e01b909104166005148061062e575060066105cb565b600060056105cb565b60076105a7565b600481015460009060ff600160e01b90910416600a148061062e575060096105cb56fea265627a7a723158203c165ce1b780ff4dbc007f949470084d045873490e73fbaf12e46f30def0567b64736f6c63430005110032"

# refering to the deploy coontract
KeepRandomBeaconOperator = web3.eth.contract(address=address, abi=abi)
# TokenGrant

abi=[{'inputs': [{'internalType': 'address',
    'name': '_tokenAddress',
    'type': 'address'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'constructor'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'grantManager',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'stakingContract',
    'type': 'address'}],
  'name': 'StakingContractAuthorized',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': False,
    'internalType': 'uint256',
    'name': 'id',
    'type': 'uint256'}],
  'name': 'TokenGrantCreated',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': False,
    'internalType': 'uint256',
    'name': 'id',
    'type': 'uint256'}],
  'name': 'TokenGrantRevoked',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'uint256',
    'name': 'grantId',
    'type': 'uint256'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'}],
  'name': 'TokenGrantStaked',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'uint256',
    'name': 'grantId',
    'type': 'uint256'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'}],
  'name': 'TokenGrantWithdrawn',
  'type': 'event'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_stakingContract',
    'type': 'address'}],
  'name': 'authorizeStakingContract',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256',
    'name': '_grantId',
    'type': 'uint256'}],
  'name': 'availableToStake',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': '_owner', 'type': 'address'}],
  'name': 'balanceOf',
  'outputs': [{'internalType': 'uint256',
    'name': 'balance',
    'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'name': 'balances',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'cancelRevokedStake',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'cancelStake',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}],
  'name': 'getGrant',
  'outputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'withdrawn', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'staked', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'revokedAmount', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'revokedAt', 'type': 'uint256'},
   {'internalType': 'address', 'name': 'grantee', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'}],
  'name': 'getGrantStakeDetails',
  'outputs': [{'internalType': 'uint256',
    'name': 'grantId',
    'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'},
   {'internalType': 'address', 'name': 'stakingContract', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}],
  'name': 'getGrantUnlockingSchedule',
  'outputs': [{'internalType': 'address',
    'name': 'grantManager',
    'type': 'address'},
   {'internalType': 'uint256', 'name': 'duration', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'start', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'cliff', 'type': 'uint256'},
   {'internalType': 'address', 'name': 'policy', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': 'grantee',
    'type': 'address'}],
  'name': 'getGranteeOperators',
  'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_granteeOrGrantManager',
    'type': 'address'}],
  'name': 'getGrants',
  'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'},
   {'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'name': 'grantIndices',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'name': 'grantStakes',
  'outputs': [{'internalType': 'contract TokenGrantStake',
    'name': '',
    'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'},
   {'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'name': 'granteesToOperators',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'name': 'grants',
  'outputs': [{'internalType': 'address',
    'name': 'grantManager',
    'type': 'address'},
   {'internalType': 'address', 'name': 'grantee', 'type': 'address'},
   {'internalType': 'uint256', 'name': 'revokedAt', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'revokedAmount', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'revokedWithdrawn', 'type': 'uint256'},
   {'internalType': 'bool', 'name': 'revocable', 'type': 'bool'},
   {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'duration', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'start', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'cliff', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'withdrawn', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'staked', 'type': 'uint256'},
   {'internalType': 'contract GrantStakingPolicy',
    'name': 'stakingPolicy',
    'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'numGrants',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address', 'name': '_from', 'type': 'address'},
   {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'},
   {'internalType': 'address', 'name': '_token', 'type': 'address'},
   {'internalType': 'bytes', 'name': '_extraData', 'type': 'bytes'}],
  'name': 'receiveApproval',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'recoverStake',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}],
  'name': 'revoke',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'},
   {'internalType': 'address', 'name': '_stakingContract', 'type': 'address'},
   {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'},
   {'internalType': 'bytes', 'name': '_extraData', 'type': 'bytes'}],
  'name': 'stake',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_address',
    'type': 'address'}],
  'name': 'stakeBalanceOf',
  'outputs': [{'internalType': 'uint256',
    'name': 'balance',
    'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'token',
  'outputs': [{'internalType': 'contract ERC20Burnable',
    'name': '',
    'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'undelegate',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'undelegateRevoked',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}],
  'name': 'unlockedAmount',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}],
  'name': 'withdraw',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}],
  'name': 'withdrawRevoked',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}],
  'name': 'withdrawable',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'}]
address = web3.toChecksumAddress("0xb64649fe00f8Ef5187d09d109C6F38f13C7CF857")
# bytecode = "0x60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032"
# bytecode = "0x60806040526000805460ff191690553480156200001b57600080fd5b506200003463deadbeef6001600160e01b036200003a16565b620000f4565b6001600160a01b038116620000815760405162461bcd60e51b8152600401808060200182810382526023815260200180620032ed6023913960400191505060405180910390fd5b60005460ff1615620000c55760405162461bcd60e51b8152600401808060200182810382526025815260200180620033106025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b6131e980620001046000396000f3fe60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e"
# bytecode = "0x610793610026600b82828239805160001a60731461001957fe5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600436106101ce5760003560e01c80639df1b34611610103578063c28eab40116100a1578063e0dfa4b31161007b578063e0dfa4b314610523578063ef2bd3d014610540578063f09911ee1461055d578063fb0611ff14610587576101ce565b8063c28eab40146104bf578063cb4536ad146104e9578063dcf5c88c14610506576101ce565b8063afb8e293116100dd578063afb8e2931461044b578063b0b6855a14610468578063b5e6a0a014610485578063b65fb6cb146104a2576101ce565b80639df1b346146103e7578063a2f9a98014610404578063a6fd0b5614610421576101ce565b806348312fa311610170578063652d34301161014a578063652d3430146103595780636fdbb3c414610376578063761275bf146103a05780638be5e97f146103bd576101ce565b806348312fa3146102f55780635a332575146103125780635dd33d991461032f576101ce565b8063171b2a05116101ac578063171b2a051461025a57806327f2744914610284578063375ec420146102a1578063429fcb0d146102cb576101ce565b8063056256a8146101d35780630f2c6355146101ff57806316cddf4e14610230575b600080fd5b8180156101df57600080fd5b506101fd600480360360208110156101f657600080fd5b50356105a4565b005b61021c6004803603602081101561021557600080fd5b50356105c6565b604080519115158252519081900360200190f35b81801561023c57600080fd5b506101fd6004803603602081101561025357600080fd5b50356105e6565b81801561026657600080fd5b506101fd6004803603602081101561027d57600080fd5b50356105ed565b61021c6004803603602081101561029a57600080fd5b50356105f4565b8180156102ad57600080fd5b506101fd600480360360208110156102c457600080fd5b50356105fd565b8180156102d757600080fd5b506101fd600480360360208110156102ee57600080fd5b5035610604565b61021c6004803603602081101561030b57600080fd5b503561060b565b61021c6004803603602081101561032857600080fd5b5035610634565b81801561033b57600080fd5b506101fd6004803603602081101561035257600080fd5b5035610671565b61021c6004803603602081101561036f57600080fd5b5035610678565b81801561038257600080fd5b506101fd6004803603602081101561039957600080fd5b5035610680565b61021c600480360360208110156103b657600080fd5b5035610687565b8180156103c957600080fd5b506101fd600480360360208110156103e057600080fd5b5035610690565b61021c600480360360208110156103fd57600080fd5b5035610697565b61021c6004803603602081101561041a57600080fd5b50356106a0565b81801561042d57600080fd5b506101fd6004803603602081101561044457600080fd5b50356106a9565b61021c6004803603602081101561046157600080fd5b50356106b0565b61021c6004803603602081101561047e57600080fd5b50356106d4565b61021c6004803603602081101561049b57600080fd5b50356106dd565b61021c600480360360208110156104b857600080fd5b50356106e6565b8180156104cb57600080fd5b506101fd600480360360208110156104e257600080fd5b50356106ef565b61021c600480360360208110156104ff57600080fd5b50356106f6565b61021c6004803603602081101561051c57600080fd5b50356106ff565b61021c6004803603602081101561053957600080fd5b5035610708565b61021c6004803603602081101561055657600080fd5b503561072b565b81801561056957600080fd5b506101fd6004803603602081101561058057600080fd5b5035610734565b61021c6004803603602081101561059d57600080fd5b503561073b565b600b5b81600401601c6101000a81548160ff021916908360ff16021790555050565b600060045b6004830154600160e01b900460ff9081169116149050919050565b60016105a7565b60086105a7565b600060026105cb565b60046105a7565b60056105a7565b600481015460009060ff600160e01b909104166001148061062e575060026105cb565b92915050565b600481015460009060ff600160e01b90910416600b14806106645750600482015460ff600160e01b909104166007145b8061062e575060036105cb565b600a6105a7565b6000806105cb565b60036105a7565b600060086105cb565b60026105a7565b6000600b6105cb565b600060096105cb565b60066105a7565b6000600480830154600160e01b900460ff9081169116148061062e575060086105cb565b600060076105cb565b600060016105cb565b600060036105cb565b60096105a7565b600060066105cb565b6000600a6105cb565b600481015460009060ff600160e01b909104166005148061062e575060066105cb565b600060056105cb565b60076105a7565b600481015460009060ff600160e01b90910416600a148061062e575060096105cb56fea265627a7a723158203c165ce1b780ff4dbc007f949470084d045873490e73fbaf12e46f30def0567b64736f6c63430005110032"

# refering to the deploy coontract
TokenGrant = web3.eth.contract(address=address, abi=abi)

abi=[{'inputs': [{'internalType': 'address',
    'name': '_masterBondedECDSAKeepAddress',
    'type': 'address'},
   {'internalType': 'address',
    'name': '_sortitionPoolFactory',
    'type': 'address'},
   {'internalType': 'address', 'name': '_tokenStaking', 'type': 'address'},
   {'internalType': 'address', 'name': '_keepBonding', 'type': 'address'},
   {'internalType': 'address', 'name': '_randomBeacon', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'constructor'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'keepAddress',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address[]',
    'name': 'members',
    'type': 'address[]'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'owner',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'application',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'honestThreshold',
    'type': 'uint256'}],
  'name': 'BondedECDSAKeepCreated',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'application',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'sortitionPool',
    'type': 'address'}],
  'name': 'SortitionPoolCreated',
  'type': 'event'},
 {'payable': True, 'stateMutability': 'payable', 'type': 'fallback'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': '_relayEntry',
    'type': 'uint256'}],
  'name': '__beaconCallback',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_delegatedAuthorityRecipient',
    'type': 'address'}],
  'name': '__isRecognized',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'balanceOf',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'callbackGas',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_application',
    'type': 'address'}],
  'name': 'createSortitionPool',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}],
  'name': 'getKeepAtIndex',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'getKeepCount',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': '_keep', 'type': 'address'}],
  'name': 'getKeepOpenedTimestamp',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_application',
    'type': 'address'}],
  'name': 'getSortitionPool',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_application',
    'type': 'address'}],
  'name': 'getSortitionPoolWeight',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'groupSelectionSeed',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'hasMinimumStake',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'isOperatorAuthorized',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_application', 'type': 'address'}],
  'name': 'isOperatorEligible',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_application', 'type': 'address'}],
  'name': 'isOperatorRegistered',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_application', 'type': 'address'}],
  'name': 'isOperatorUpToDate',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'name': 'keeps',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'masterKeepAddress',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'minimumBond',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'newEntryFeeEstimate',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'newGroupSelectionSeedFee',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': '_groupSize',
    'type': 'uint256'},
   {'internalType': 'uint256', 'name': '_honestThreshold', 'type': 'uint256'},
   {'internalType': 'address', 'name': '_owner', 'type': 'address'},
   {'internalType': 'uint256', 'name': '_bond', 'type': 'uint256'},
   {'internalType': 'uint256',
    'name': '_stakeLockDuration',
    'type': 'uint256'}],
  'name': 'openKeep',
  'outputs': [{'internalType': 'address',
    'name': 'keepAddress',
    'type': 'address'}],
  'payable': True,
  'stateMutability': 'payable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'openKeepFeeEstimate',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'poolStakeWeightDivisor',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_application',
    'type': 'address'}],
  'name': 'registerMemberCandidate',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [],
  'name': 'requestNewGroupSelectionSeed',
  'outputs': [],
  'payable': True,
  'stateMutability': 'payable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'reseedPool',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': '_minimumBondableValue',
    'type': 'uint256'},
   {'internalType': 'uint256', 'name': '_groupSize', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': '_honestThreshold', 'type': 'uint256'}],
  'name': 'setMinimumBondableValue',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_application', 'type': 'address'}],
  'name': 'updateOperatorStatus',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'}]
address = web3.toChecksumAddress("0x9EcCf03dFBDa6A5E50d7aBA14e0c60c2F6c575E6")
# bytecode = "0x60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032"
# bytecode = "0x60806040526000805460ff191690553480156200001b57600080fd5b506200003463deadbeef6001600160e01b036200003a16565b620000f4565b6001600160a01b038116620000815760405162461bcd60e51b8152600401808060200182810382526023815260200180620032ed6023913960400191505060405180910390fd5b60005460ff1615620000c55760405162461bcd60e51b8152600401808060200182810382526025815260200180620033106025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b6131e980620001046000396000f3fe60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e"
# bytecode = "0x610793610026600b82828239805160001a60731461001957fe5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600436106101ce5760003560e01c80639df1b34611610103578063c28eab40116100a1578063e0dfa4b31161007b578063e0dfa4b314610523578063ef2bd3d014610540578063f09911ee1461055d578063fb0611ff14610587576101ce565b8063c28eab40146104bf578063cb4536ad146104e9578063dcf5c88c14610506576101ce565b8063afb8e293116100dd578063afb8e2931461044b578063b0b6855a14610468578063b5e6a0a014610485578063b65fb6cb146104a2576101ce565b80639df1b346146103e7578063a2f9a98014610404578063a6fd0b5614610421576101ce565b806348312fa311610170578063652d34301161014a578063652d3430146103595780636fdbb3c414610376578063761275bf146103a05780638be5e97f146103bd576101ce565b806348312fa3146102f55780635a332575146103125780635dd33d991461032f576101ce565b8063171b2a05116101ac578063171b2a051461025a57806327f2744914610284578063375ec420146102a1578063429fcb0d146102cb576101ce565b8063056256a8146101d35780630f2c6355146101ff57806316cddf4e14610230575b600080fd5b8180156101df57600080fd5b506101fd600480360360208110156101f657600080fd5b50356105a4565b005b61021c6004803603602081101561021557600080fd5b50356105c6565b604080519115158252519081900360200190f35b81801561023c57600080fd5b506101fd6004803603602081101561025357600080fd5b50356105e6565b81801561026657600080fd5b506101fd6004803603602081101561027d57600080fd5b50356105ed565b61021c6004803603602081101561029a57600080fd5b50356105f4565b8180156102ad57600080fd5b506101fd600480360360208110156102c457600080fd5b50356105fd565b8180156102d757600080fd5b506101fd600480360360208110156102ee57600080fd5b5035610604565b61021c6004803603602081101561030b57600080fd5b503561060b565b61021c6004803603602081101561032857600080fd5b5035610634565b81801561033b57600080fd5b506101fd6004803603602081101561035257600080fd5b5035610671565b61021c6004803603602081101561036f57600080fd5b5035610678565b81801561038257600080fd5b506101fd6004803603602081101561039957600080fd5b5035610680565b61021c600480360360208110156103b657600080fd5b5035610687565b8180156103c957600080fd5b506101fd600480360360208110156103e057600080fd5b5035610690565b61021c600480360360208110156103fd57600080fd5b5035610697565b61021c6004803603602081101561041a57600080fd5b50356106a0565b81801561042d57600080fd5b506101fd6004803603602081101561044457600080fd5b50356106a9565b61021c6004803603602081101561046157600080fd5b50356106b0565b61021c6004803603602081101561047e57600080fd5b50356106d4565b61021c6004803603602081101561049b57600080fd5b50356106dd565b61021c600480360360208110156104b857600080fd5b50356106e6565b8180156104cb57600080fd5b506101fd600480360360208110156104e257600080fd5b50356106ef565b61021c600480360360208110156104ff57600080fd5b50356106f6565b61021c6004803603602081101561051c57600080fd5b50356106ff565b61021c6004803603602081101561053957600080fd5b5035610708565b61021c6004803603602081101561055657600080fd5b503561072b565b81801561056957600080fd5b506101fd6004803603602081101561058057600080fd5b5035610734565b61021c6004803603602081101561059d57600080fd5b503561073b565b600b5b81600401601c6101000a81548160ff021916908360ff16021790555050565b600060045b6004830154600160e01b900460ff9081169116149050919050565b60016105a7565b60086105a7565b600060026105cb565b60046105a7565b60056105a7565b600481015460009060ff600160e01b909104166001148061062e575060026105cb565b92915050565b600481015460009060ff600160e01b90910416600b14806106645750600482015460ff600160e01b909104166007145b8061062e575060036105cb565b600a6105a7565b6000806105cb565b60036105a7565b600060086105cb565b60026105a7565b6000600b6105cb565b600060096105cb565b60066105a7565b6000600480830154600160e01b900460ff9081169116148061062e575060086105cb565b600060076105cb565b600060016105cb565b600060036105cb565b60096105a7565b600060066105cb565b6000600a6105cb565b600481015460009060ff600160e01b909104166005148061062e575060066105cb565b600060056105cb565b60076105a7565b600481015460009060ff600160e01b90910416600a148061062e575060096105cb56fea265627a7a723158203c165ce1b780ff4dbc007f949470084d045873490e73fbaf12e46f30def0567b64736f6c63430005110032"

# refering to the deploy coontract
abi=[{'inputs': [{'internalType': 'address',
    'name': 'registryAddress',
    'type': 'address'},
   {'internalType': 'address',
    'name': 'tokenStakingAddress',
    'type': 'address'},
   {'internalType': 'address',
    'name': 'tokenGrantAddress',
    'type': 'address'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'constructor'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'holder',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'sortitionPool',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'referenceID',
    'type': 'uint256'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'}],
  'name': 'BondCreated',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'uint256',
    'name': 'referenceID',
    'type': 'uint256'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'newHolder',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'newReferenceID',
    'type': 'uint256'}],
  'name': 'BondReassigned',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'uint256',
    'name': 'referenceID',
    'type': 'uint256'}],
  'name': 'BondReleased',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'uint256',
    'name': 'referenceID',
    'type': 'uint256'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'destination',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'}],
  'name': 'BondSeized',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'beneficiary',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'}],
  'name': 'UnbondedValueDeposited',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'beneficiary',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'amount',
    'type': 'uint256'}],
  'name': 'UnbondedValueWithdrawn',
  'type': 'event'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_poolAddress', 'type': 'address'}],
  'name': 'authorizeSortitionPoolContract',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'authorizerOf',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'address', 'name': 'bondCreator', 'type': 'address'},
   {'internalType': 'address',
    'name': 'authorizedSortitionPool',
    'type': 'address'}],
  'name': 'availableUnbondedValue',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'beneficiaryOf',
  'outputs': [{'internalType': 'address payable',
    'name': '',
    'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'address', 'name': 'holder', 'type': 'address'},
   {'internalType': 'uint256', 'name': 'referenceID', 'type': 'uint256'}],
  'name': 'bondAmount',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'address', 'name': 'holder', 'type': 'address'},
   {'internalType': 'uint256', 'name': 'referenceID', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'},
   {'internalType': 'address',
    'name': 'authorizedSortitionPool',
    'type': 'address'}],
  'name': 'createBond',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_poolAddress', 'type': 'address'}],
  'name': 'deauthorizeSortitionPoolContract',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'}],
  'name': 'deposit',
  'outputs': [],
  'payable': True,
  'stateMutability': 'payable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'uint256', 'name': 'referenceID', 'type': 'uint256'}],
  'name': 'freeBond',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_poolAddress', 'type': 'address'}],
  'name': 'hasSecondaryAuthorization',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address',
    'name': '_operatorContract',
    'type': 'address'}],
  'name': 'isAuthorizedForOperator',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'uint256', 'name': 'referenceID', 'type': 'uint256'},
   {'internalType': 'address', 'name': 'newHolder', 'type': 'address'},
   {'internalType': 'uint256', 'name': 'newReferenceID', 'type': 'uint256'}],
  'name': 'reassignBond',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': 'operator',
    'type': 'address'},
   {'internalType': 'uint256', 'name': 'referenceID', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'},
   {'internalType': 'address payable',
    'name': 'destination',
    'type': 'address'}],
  'name': 'seizeBond',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'name': 'unbondedValue',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'},
   {'internalType': 'address', 'name': 'operator', 'type': 'address'}],
  'name': 'withdraw',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'},
   {'internalType': 'address', 'name': 'operator', 'type': 'address'},
   {'internalType': 'address', 'name': 'managedGrant', 'type': 'address'}],
  'name': 'withdrawAsManagedGrantee',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'}]
address = web3.toChecksumAddress("0x60535A59B4e71F908f3fEB0116F450703FB35eD8")
# bytecode = "0x60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032"
# bytecode = "0x60806040526000805460ff191690553480156200001b57600080fd5b506200003463deadbeef6001600160e01b036200003a16565b620000f4565b6001600160a01b038116620000815760405162461bcd60e51b8152600401808060200182810382526023815260200180620032ed6023913960400191505060405180910390fd5b60005460ff1615620000c55760405162461bcd60e51b8152600401808060200182810382526025815260200180620033106025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b6131e980620001046000396000f3fe60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e"
# bytecode = "0x610793610026600b82828239805160001a60731461001957fe5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600436106101ce5760003560e01c80639df1b34611610103578063c28eab40116100a1578063e0dfa4b31161007b578063e0dfa4b314610523578063ef2bd3d014610540578063f09911ee1461055d578063fb0611ff14610587576101ce565b8063c28eab40146104bf578063cb4536ad146104e9578063dcf5c88c14610506576101ce565b8063afb8e293116100dd578063afb8e2931461044b578063b0b6855a14610468578063b5e6a0a014610485578063b65fb6cb146104a2576101ce565b80639df1b346146103e7578063a2f9a98014610404578063a6fd0b5614610421576101ce565b806348312fa311610170578063652d34301161014a578063652d3430146103595780636fdbb3c414610376578063761275bf146103a05780638be5e97f146103bd576101ce565b806348312fa3146102f55780635a332575146103125780635dd33d991461032f576101ce565b8063171b2a05116101ac578063171b2a051461025a57806327f2744914610284578063375ec420146102a1578063429fcb0d146102cb576101ce565b8063056256a8146101d35780630f2c6355146101ff57806316cddf4e14610230575b600080fd5b8180156101df57600080fd5b506101fd600480360360208110156101f657600080fd5b50356105a4565b005b61021c6004803603602081101561021557600080fd5b50356105c6565b604080519115158252519081900360200190f35b81801561023c57600080fd5b506101fd6004803603602081101561025357600080fd5b50356105e6565b81801561026657600080fd5b506101fd6004803603602081101561027d57600080fd5b50356105ed565b61021c6004803603602081101561029a57600080fd5b50356105f4565b8180156102ad57600080fd5b506101fd600480360360208110156102c457600080fd5b50356105fd565b8180156102d757600080fd5b506101fd600480360360208110156102ee57600080fd5b5035610604565b61021c6004803603602081101561030b57600080fd5b503561060b565b61021c6004803603602081101561032857600080fd5b5035610634565b81801561033b57600080fd5b506101fd6004803603602081101561035257600080fd5b5035610671565b61021c6004803603602081101561036f57600080fd5b5035610678565b81801561038257600080fd5b506101fd6004803603602081101561039957600080fd5b5035610680565b61021c600480360360208110156103b657600080fd5b5035610687565b8180156103c957600080fd5b506101fd600480360360208110156103e057600080fd5b5035610690565b61021c600480360360208110156103fd57600080fd5b5035610697565b61021c6004803603602081101561041a57600080fd5b50356106a0565b81801561042d57600080fd5b506101fd6004803603602081101561044457600080fd5b50356106a9565b61021c6004803603602081101561046157600080fd5b50356106b0565b61021c6004803603602081101561047e57600080fd5b50356106d4565b61021c6004803603602081101561049b57600080fd5b50356106dd565b61021c600480360360208110156104b857600080fd5b50356106e6565b8180156104cb57600080fd5b506101fd600480360360208110156104e257600080fd5b50356106ef565b61021c600480360360208110156104ff57600080fd5b50356106f6565b61021c6004803603602081101561051c57600080fd5b50356106ff565b61021c6004803603602081101561053957600080fd5b5035610708565b61021c6004803603602081101561055657600080fd5b503561072b565b81801561056957600080fd5b506101fd6004803603602081101561058057600080fd5b5035610734565b61021c6004803603602081101561059d57600080fd5b503561073b565b600b5b81600401601c6101000a81548160ff021916908360ff16021790555050565b600060045b6004830154600160e01b900460ff9081169116149050919050565b60016105a7565b60086105a7565b600060026105cb565b60046105a7565b60056105a7565b600481015460009060ff600160e01b909104166001148061062e575060026105cb565b92915050565b600481015460009060ff600160e01b90910416600b14806106645750600482015460ff600160e01b909104166007145b8061062e575060036105cb565b600a6105a7565b6000806105cb565b60036105a7565b600060086105cb565b60026105a7565b6000600b6105cb565b600060096105cb565b60066105a7565b6000600480830154600160e01b900460ff9081169116148061062e575060086105cb565b600060076105cb565b600060016105cb565b600060036105cb565b60096105a7565b600060066105cb565b6000600a6105cb565b600481015460009060ff600160e01b909104166005148061062e575060066105cb565b600060056105cb565b60076105a7565b600481015460009060ff600160e01b90910416600a148061062e575060096105cb56fea265627a7a723158203c165ce1b780ff4dbc007f949470084d045873490e73fbaf12e46f30def0567b64736f6c63430005110032"

# refering to the deploy coontract
KeepBonding = web3.eth.contract(address=address, abi=abi)

address = web3.toChecksumAddress("0x9EcCf03dFBDa6A5E50d7aBA14e0c60c2F6c575E6")
#bytecode = "0x60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032"
#bytecode = "0x60806040526000805460ff191690553480156200001b57600080fd5b506200003463deadbeef6001600160e01b036200003a16565b620000f4565b6001600160a01b038116620000815760405162461bcd60e51b8152600401808060200182810382526023815260200180620032ed6023913960400191505060405180910390fd5b60005460ff1615620000c55760405162461bcd60e51b8152600401808060200182810382526025815260200180620033106025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b6131e980620001046000396000f3fe60806040526004361061022f5760003560e01c806391d165e31161012e578063c4d66de8116100ab578063d9f74b0e1161006f578063d9f74b0e14610b8e578063dba4915314610e01578063ea3db25014610eb0578063f97a02fa14610ec5578063fb7c592a14610eee5761022f565b8063c4d66de8146107be578063d02fd958146107f1578063d459c41614610824578063d5eef97114610a8f578063d8d0233014610b5b5761022f565b8063994aa931116100f2578063994aa93114610642578063a81e63f714610704578063b4bd2e7a1461075b578063ba34683914610770578063c4159559146107855761022f565b806391d165e3146105b2578063946fbf4c146105c7578063951303f5146105dc57806396aab311146105f15780639894d734146106065761022f565b80632c735daa116101bc5780636e4668be116101805780636e4668be1461052c57806376ef55101461054157806385df153d1461055657806387a90d801461056b57806390a2f687146105805761022f565b80632c735daa146103f05780632d0994421461040557806335bc0ebe146104d15780634f706e44146104e65780636c3b0114146104fb5761022f565b806313f654df1161020357806313f654df1461038757806324600fc31461039c578063259b1ea3146103b1578063287b32e5146103c65780632b0bc981146103db5761022f565b806249ce751461026e578063058d37031461031f5780630c3f6acf146103465780630d5889f41461035b575b361561026c5760405162461bcd60e51b815260040180806020018281038252603b81526020018061300a603b913960400191505060405180910390fd5b005b34801561027a57600080fd5b5061026c6004803603602081101561029157600080fd5b810190602081018135600160201b8111156102ab57600080fd5b8201836020820111156102bd57600080fd5b803590602001918460018302840111600160201b831117156102de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610fbb945050505050565b34801561032b57600080fd5b50610334611156565b60408051918252519081900360200190f35b34801561035257600080fd5b506103346111db565b34801561036757600080fd5b506103706111eb565b6040805161ffff9092168252519081900360200190f35b34801561039357600080fd5b506103346111fc565b3480156103a857600080fd5b5061026c611309565b3480156103bd57600080fd5b5061026c611315565b3480156103d257600080fd5b5061026c611381565b3480156103e757600080fd5b5061026c6113d3565b3480156103fc57600080fd5b5061026c611425565b34801561041157600080fd5b5061026c600480360360a081101561042857600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b81111561045d57600080fd5b82018360208201111561046f57600080fd5b803590602001918460018302840111600160201b8311171561049057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611477945050505050565b3480156104dd57600080fd5b50610334611578565b3480156104f257600080fd5b5061026c6115cc565b34801561050757600080fd5b5061051061161e565b604080516001600160a01b039092168252519081900360200190f35b34801561053857600080fd5b5061033461162d565b34801561054d57600080fd5b50610370611681565b34801561056257600080fd5b5061037061168b565b34801561057757600080fd5b5061033461169b565b34801561058c57600080fd5b506105956117a9565b6040805167ffffffffffffffff9092168252519081900360200190f35b3480156105be57600080fd5b5061026c6117c0565b3480156105d357600080fd5b50610334611812565b3480156105e857600080fd5b50610334611866565b3480156105fd57600080fd5b5061026c611877565b34801561061257600080fd5b5061026c6004803603604081101561062957600080fd5b506001600160c01b0319813581169160200135166118c9565b34801561064e57600080fd5b5061026c6004803603604081101561066557600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b81111561069057600080fd5b8201836020820111156106a257600080fd5b803590602001918460018302840111600160201b831117156106c357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092955061194f945050505050565b61026c600480360360c081101561071a57600080fd5b5080356001600160a01b03908116916020810135821691604082013581169160608101358216916080820135169060a0013567ffffffffffffffff16611a21565b34801561076757600080fd5b5061026c611b88565b34801561077c57600080fd5b5061026c611bda565b34801561079157600080fd5b5061026c600480360360608110156107a857600080fd5b5060ff8135169060208101359060400135611c2c565b3480156107ca57600080fd5b5061026c600480360360208110156107e157600080fd5b50356001600160a01b0316611cb2565b3480156107fd57600080fd5b506103346004803603602081101561081457600080fd5b50356001600160a01b0316611d68565b34801561083057600080fd5b5061026c600480360360e081101561084757600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b81111561087257600080fd5b82018360208201111561088457600080fd5b803590602001918460018302840111600160201b831117156108a557600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b8111156108f757600080fd5b82018360208201111561090957600080fd5b803590602001918460018302840111600160201b8311171561092a57600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b0319853516959094909350604081019250602001359050600160201b81111561098e57600080fd5b8201836020820111156109a057600080fd5b803590602001918460018302840111600160201b831117156109c157600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610a1b57600080fd5b820183602082011115610a2d57600080fd5b803590602001918460018302840111600160201b83111715610a4e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611d89945050505050565b348015610a9b57600080fd5b5061026c600480360360a0811015610ab257600080fd5b60ff8235169160208101359160408201359160608101359181019060a081016080820135600160201b811115610ae757600080fd5b820183602082011115610af957600080fd5b803590602001918460018302840111600160201b83111715610b1a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550611fcb945050505050565b348015610b6757600080fd5b5061033460048036036020811015610b7e57600080fd5b50356001600160a01b031661205d565b348015610b9a57600080fd5b5061026c6004803603610100811015610bb257600080fd5b6001600160e01b03198235169190810190604081016020820135600160201b811115610bdd57600080fd5b820183602082011115610bef57600080fd5b803590602001918460018302840111600160201b83111715610c1057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295949360208101935035915050600160201b811115610c6257600080fd5b820183602082011115610c7457600080fd5b803590602001918460018302840111600160201b83111715610c9557600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092956001600160e01b03198535169560ff60208701351695919450925060608101915060400135600160201b811115610d0057600080fd5b820183602082011115610d1257600080fd5b803590602001918460018302840111600160201b83111715610d3357600080fd5b91908080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525092958435959094909350604081019250602001359050600160201b811115610d8d57600080fd5b820183602082011115610d9f57600080fd5b803590602001918460018302840111600160201b83111715610dc057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550612072945050505050565b348015610e0d57600080fd5b50610e166122c2565b60405180846001600160c01b0319166001600160c01b031916815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610e73578181015183820152602001610e5b565b50505050905090810190601f168015610ea05780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b348015610ebc57600080fd5b5061026c612428565b348015610ed157600080fd5b50610eda61247a565b604080519115158252519081900360200190f35b348015610efa57600080fd5b5061026c60048036036060811015610f1157600080fd5b6001600160c01b03198235169190810190604081016020820135600160201b811115610f3c57600080fd5b820183602082011115610f4e57600080fd5b803590602001918460018302840111600160201b83111715610f6f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550505090356001600160a01b031691506124ce9050565b6040805163ad91ce1f60e01b8152600160048201529051339173__$ae2abe2ba05898bb347c6a93c12322aec0$__9163ad91ce1f91602480820192602092909190829003018186803b15801561101057600080fd5b505af4158015611024573d6000803e3d6000fd5b505050506040513d602081101561103a57600080fd5b50516001600160a01b0316146110815760405162461bcd60e51b81526004018080602001828103825260288152602001806130456028913960400191505060405180910390fd5b60408051635f3c5d8960e01b81526001600482018181526024830193845284516044840152845173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__94635f3c5d8994879392606490910190602085019080838360005b838110156110f05781810151838201526020016110d8565b50505050905090810190601f16801561111d5780820380516001836020036101000a031916815260200191505b50935050505060006040518083038186803b15801561113b57600080fd5b505af415801561114f573d6000803e3d6000fd5b5050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__63a880784890916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b505af41580156111be573d6000803e3d6000fd5b505050506040513d60208110156111d457600080fd5b5051905090565b600554600160e01b900460ff1690565b600654600160201b900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__63fb0611ff90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561125057600080fd5b505af4158015611264573d6000803e3d6000fd5b505050506040513d602081101561127a57600080fd5b50516112b75760405162461bcd60e51b815260040180806020018281038252602981526020018061315f6029913960400191505060405180910390fd5b604080516350ef3aa160e01b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__916350ef3aa1916024808301926020929190829003018186803b1580156111aa57600080fd5b61131360016125f5565b565b6040805163426e16c160e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163426e16c1916024808301926000929190829003018186803b15801561136757600080fd5b505af415801561137b573d6000803e3d6000fd5b50505050565b6040805163077aceb960e31b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91633bd675c8916024808301926000929190829003018186803b15801561136757600080fd5b6040805163439b7be160e11b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91638736f7c2916024808301926000929190829003018186803b15801561136757600080fd5b60408051631754228360e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91632ea84506916024808301926000929190829003018186803b15801561136757600080fd5b600173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__63fb12d9df909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360005b8381101561150a5781810151838201526020016114f2565b50505050905090810190601f1680156115375780820380516001836020036101000a031916815260200191505b5097505050505050505060006040518083038186803b15801561155957600080fd5b505af415801561156d573d6000803e3d6000fd5b505050505050505050565b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__6391f88c8590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b604080516361f036d360e01b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__916361f036d3916024808301926000929190829003018186803b15801561136757600080fd5b600b546001600160a01b031690565b6000600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__63e86e97b690916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60065461ffff1690565b60065462010000900461ffff1690565b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156116ef57600080fd5b505af4158015611703573d6000803e3d6000fd5b505050506040513d602081101561171957600080fd5b5051156117575760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60408051631ec664f560e21b815260016004820152905173__$ae2abe2ba05898bb347c6a93c12322aec0$__91637b1993d4916024808301926020929190829003018186803b1580156111aa57600080fd5b600554600160a01b900467ffffffffffffffff1690565b60408051634e40547560e11b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__91639c80a8ea916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$ae2abe2ba05898bb347c6a93c12322aec0$__637949c2d290916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b60006118726001612812565b905090565b6040805163a221542160e01b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__9163a2215421916024808301926000929190829003018186803b15801561136757600080fd5b60408051632d0c21bf60e01b8152600160048201526001600160c01b0319808516602483015283166044820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91632d0c21bf916064808301926000929190829003018186803b15801561193357600080fd5b505af4158015611947573d6000803e3d6000fd5b505050505050565b604051632cac94ef60e01b81526001600482018181526001600160c01b03198516602484015260606044840190815284516064850152845173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94632cac94ef94938893889391929091608490910190602085019080838360005b838110156119d55781810151838201526020016119bd565b50505050905090810190601f168015611a025780820380516001836020036101000a031916815260200191505b5094505050505060006040518083038186803b15801561193357600080fd5b60005460ff16611a625760405162461bcd60e51b815260040180806020018281038252602d815260200180613188602d913960400191505060405180910390fd5b60005461010090046001600160a01b03163314611ab05760405162461bcd60e51b81526004018080602001828103825260268152602001806131396026913960400191505060405180910390fd5b600180546001600160a01b03199081166001600160a01b03898116919091178355600280548316898316179055600380548316888316179055600480548316878316178155600580549093169186169190911790915560408051632851e9dd60e01b81529182019290925267ffffffffffffffff83166024820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__91632851e9dd916044808301926000929190829003018186803b158015611b6857600080fd5b505af4158015611b7c573d6000803e3d6000fd5b50505050505050505050565b604080516324e8e19960e21b815260016004820152905173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__916393a38664916024808301926000929190829003018186803b15801561136757600080fd5b604080516304bfa27760e01b815260016004820152905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__916304bfa277916024808301926000929190829003018186803b15801561136757600080fd5b60408051631e3435d560e11b81526001600482015260ff851660248201526044810184905260648101839052905173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__91633c686baa916084808301926000929190829003018186803b158015611c9557600080fd5b505af4158015611ca9573d6000803e3d6000fd5b50505050505050565b6001600160a01b038116611cf75760405162461bcd60e51b8152600401808060200182810382526023815260200180612fbb6023913960400191505060405180910390fd5b60005460ff1615611d395760405162461bcd60e51b81526004018080602001828103825260258152602001806131146025913960400191505060405180910390fd5b6000805460ff196001600160a01b0390931661010002610100600160a81b031990911617919091166001179055565b600080611d7d6001848363ffffffff61282916565b5090925050505b919050565b604051636c7e2b9d60e01b81526001600482018181526001600160e01b0319808b1660248501528716608484015260c48301859052610100604484019081528951610104850152895173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__94636c7e2b9d94938d938d938d938d938d938d938d93606481019160a482019160e48101916101249091019060208d019080838360005b83811015611e36578181015183820152602001611e1e565b50505050905090810190601f168015611e635780820380516001836020036101000a031916815260200191505b5085810384528a5181528a516020918201918c019080838360005b83811015611e96578181015183820152602001611e7e565b50505050905090810190601f168015611ec35780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b83811015611ef6578181015183820152602001611ede565b50505050905090810190601f168015611f235780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b83811015611f56578181015183820152602001611f3e565b50505050905090810190601f168015611f835780820380516001836020036101000a031916815260200191505b509c5050505050505050505050505060006040518083038186803b158015611faa57600080fd5b505af4158015611fbe573d6000803e3d6000fd5b5050505050505050505050565b600173__$791b9b11b3588ea33e7eb9b4a1e59b645c$__634941676c909187878787876040518763ffffffff1660e01b8152600401808781526020018660ff1660ff16815260200185815260200184815260200183815260200180602001828103825283818151815260200191508051906020019080838360008381101561150a5781810151838201526020016114f2565b600080611d7d6001848163ffffffff61282916565b60405163d745519360e01b81526001600482018181526001600160e01b0319808c1660248501528816608484015260ff871660a484015260e48301859052610120604484019081528a516101248501528a5173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9463d745519394938e938e938e938e938e938e938e938e939291606482019160c4810191610104820191610144019060208e019080838360005b8381101561212b578181015183820152602001612113565b50505050905090810190601f1680156121585780820380516001836020036101000a031916815260200191505b5085810384528b5181528b516020918201918d019080838360005b8381101561218b578181015183820152602001612173565b50505050905090810190601f1680156121b85780820380516001836020036101000a031916815260200191505b5085810383528851815288516020918201918a019080838360005b838110156121eb5781810151838201526020016121d3565b50505050905090810190601f1680156122185780820380516001836020036101000a031916815260200191505b50858103825286518152865160209182019188019080838360005b8381101561224b578181015183820152602001612233565b50505050905090810190601f1680156122785780820380516001836020036101000a031916815260200191505b509d505050505050505050505050505060006040518083038186803b1580156122a057600080fd5b505af41580156122b4573d6000803e3d6000fd5b505050505050505050505050565b6000806060600173__$7369af7e716df07b29b2b0459c9383ea05$__6348312fa390916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b15801561231957600080fd5b505af415801561232d573d6000803e3d6000fd5b505050506040513d602081101561234357600080fd5b5051156123815760405162461bcd60e51b8152600401808060200182810382526041815260200180612f7a6041913960600191505060405180910390fd5b60165460175460188054604080516020601f6002600019600187161561010002019095169490940493840181900481028201810190925282815260c09590951b949183918301828280156124165780601f106123eb57610100808354040283529160200191612416565b820191906000526020600020905b8154815290600101906020018083116123f957829003601f168201915b50505050509050925092509250909192565b60408051632ec8740960e21b815260016004820152905173__$94ce0c0c748aa9d3fdc8d093f833a41c64$__9163bb21d024916024808301926000929190829003018186803b15801561136757600080fd5b6000600173__$7369af7e716df07b29b2b0459c9383ea05$__630f2c635590916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156111aa57600080fd5b6005546001600160a01b031633146125175760405162461bcd60e51b815260040180806020018281038252603e8152602001806130d6603e913960400191505060405180910390fd5b604051630d806ee760e41b81526001600482018181526001600160c01b0319861660248401526001600160a01b038416606484015260806044840190815285516084850152855173__$2aa53b365dbc2200fd3eefe41e32f5c1c9$__9463d806ee70949389938993899360a40190602086019080838360005b838110156125a8578181015183820152602001612590565b50505050905090810190601f1680156125d55780820380516001836020036101000a031916815260200191505b509550505050505060006040518083038186803b158015611c9557600080fd5b336000908152601882016020908152604091829020548251635a33257560e01b8152600481018590529251909273__$7369af7e716df07b29b2b0459c9383ea05$__92635a33257592602480840193829003018186803b15801561265857600080fd5b505af415801561266c573d6000803e3d6000fd5b505050506040513d602081101561268257600080fd5b50516126d5576040805162461bcd60e51b815260206004820152601b60248201527f436f6e7472616374206e6f7420796574207465726d696e617465640000000000604482015290519081900360640190fd5b60008111612720576040805162461bcd60e51b81526020600482015260136024820152724e6f7468696e6720746f20776974686472617760681b604482015290519081900360640190fd5b80471015612775576040805162461bcd60e51b815260206004820152601d60248201527f496e73756666696369656e7420636f6e74726163742062616c616e6365000000604482015290519081900360640190fd5b3360008181526018840160205260408082208290555190919083908381818185875af1925050503d80600081146127c8576040519150601f19603f3d011682016040523d82523d6000602084013e6127cd565b606091505b505090508061280d5760405162461bcd60e51b815260040180806020018281038252602c815260200180612fde602c913960400191505060405180910390fd5b505050565b336000908152601882016020526040902054919050565b60008060008084806128545750856001600160a01b031661284988612aa0565b6001600160a01b0316145b905060008061286289612b1f565b1180156128e957508773__$7369af7e716df07b29b2b0459c9383ea05$__63761275bf90916040518263ffffffff1660e01b81526004018082815260200191505060206040518083038186803b1580156128bb57600080fd5b505af41580156128cf573d6000803e3d6000fd5b505050506040513d60208110156128e557600080fd5b5051155b905081806128f5575080155b6129305760405162461bcd60e51b815260040180806020018281038252604881526020018061306d6048913960600191505060405180910390fd5b60008061293c8a612bd1565b6001600160a01b0316141590506000886001600160a01b031661295e8b612bd1565b6001600160a01b031614905060006129758b612cd6565b905060006129868286868987612d02565b90506129aa8161299e6129988f612d50565b89612de1565b9063ffffffff612df816565b60018d0154604080516370a0823160e01b81523060048201529051929b506000926001600160a01b03909216916370a0823191602480820192602092909190829003018186803b1580156129fd57600080fd5b505afa158015612a11573d6000803e3d6000fd5b505050506040513d6020811015612a2757600080fd5b50519050808a1115612a4a57612a438a8263ffffffff612e5916565b9950612a4f565b600099505b858015612a595750845b8015612a63575083155b15612a6c578297505b612a8e88612a828581858f63ffffffff612df816565b9063ffffffff612e5916565b98505050505050505093509350939050565b6002810154604080516331a9108f60e11b815230600482015290516000926001600160a01b031691636352211e916024808301926020929190829003018186803b158015612aed57600080fd5b505afa158015612b01573d6000803e3d6000fd5b505050506040513d6020811015612b1757600080fd5b505192915050565b600080612ba673__$86ed2a64302f7aca70b72ee6926d57c5a6$__63d565d1f16040518163ffffffff1660e01b815260040160206040518083038186803b158015612b6957600080fd5b505af4158015612b7d573d6000803e3d6000fd5b505050506040513d6020811015612b9357600080fd5b505160168501549063ffffffff612df816565b905080421015612bc857612bc0814263ffffffff612e5916565b915050611d84565b50600092915050565b600381015460408051634f558e7960e01b8152306004820152905160009283926001600160a01b0390911691634f558e7991602480820192602092909190829003018186803b158015612c2357600080fd5b505afa158015612c37573d6000803e3d6000fd5b505050506040513d6020811015612c4d57600080fd5b505115612cd0576003830154604080516331a9108f60e11b815230600482015290516001600160a01b0390921691636352211e91602480820192602092909190829003018186803b158015612ca157600080fd5b505afa158015612cb5573d6000803e3d6000fd5b505050506040513d6020811015612ccb57600080fd5b505190505b92915050565b6004810154600090612cd090600160e81b900461ffff16612cf684612d50565b9063ffffffff612eb616565b600080858015612d0f5750845b8015612d19575082155b905060008680612d265750855b80612d2e5750845b905060008115612d3b5788015b8215612d445788015b98975050505050505050565b6000612cd073__$86ed2a64302f7aca70b72ee6926d57c5a6$__63ae9eb1276040518163ffffffff1660e01b815260040160206040518083038186803b158015612d9957600080fd5b505af4158015612dad573d6000803e3d6000fd5b505050506040513d6020811015612dc357600080fd5b50516004840154600160a01b900467ffffffffffffffff1690612f20565b60008115612df157506000612cd0565b5090919050565b600082820183811015612e52576040805162461bcd60e51b815260206004820152601b60248201527f536166654d6174683a206164646974696f6e206f766572666c6f770000000000604482015290519081900360640190fd5b9392505050565b600082821115612eb0576040805162461bcd60e51b815260206004820152601e60248201527f536166654d6174683a207375627472616374696f6e206f766572666c6f770000604482015290519081900360640190fd5b50900390565b6000808211612f0c576040805162461bcd60e51b815260206004820152601a60248201527f536166654d6174683a206469766973696f6e206279207a65726f000000000000604482015290519081900360640190fd5b6000828481612f1757fe5b04949350505050565b600082612f2f57506000612cd0565b82820282848281612f3c57fe5b0414612e525760405162461bcd60e51b81526004018080602001828103825260218152602001806130b56021913960400191505060405180910390fdfe4465706f73697420686173206e6f7420796574206265656e2066756e64656420616e6420686173206e6f20617661696c61626c652066756e64696e6720696e666f466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e4661696c656420746f2073656e6420776974686472617761626c6520616d6f756e7420746f2073656e6465724465706f73697420636f6e7472616374207761732063616c6c6564207769746820756e6b6e6f776e2066756e6374696f6e2073656c6563746f722e4f6e6c792054445420686f6c6465722063616e20726571756573742066756e6465722061626f72744f6e6c792054445420686f6c6465722063616e2072656465656d20756e6c657373206465706f7369742069732061742d7465726d206f7220696e20434f5552544553595f43414c4c536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f774f6e6c79207468652076656e64696e67206d616368696e652063616e2063616c6c207472616e73666572416e6452657175657374526564656d7074696f6e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e43616c6c6572206d757374206265206465706f736974466163746f727920636f6e74726163744465706f73697420686173206e6f2066756e64732063757272656e746c792061742061756374696f6e466163746f727920696e697469616c697a6174696f6e206d7573742068617665206265656e2063616c6c65642ea265627a7a72315820ec55669da878d6a87041b177cab080114051affcfb740deffc7517dc1385feab64736f6c63430005110032466163746f72792063616e6e6f7420626520746865207a65726f20616464726573732e466163746f72792063616e206f6e6c7920626520696e697469616c697a6564206f6e63652e"
#bytecode = "0x610793610026600b82828239805160001a60731461001957fe5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600436106101ce5760003560e01c80639df1b34611610103578063c28eab40116100a1578063e0dfa4b31161007b578063e0dfa4b314610523578063ef2bd3d014610540578063f09911ee1461055d578063fb0611ff14610587576101ce565b8063c28eab40146104bf578063cb4536ad146104e9578063dcf5c88c14610506576101ce565b8063afb8e293116100dd578063afb8e2931461044b578063b0b6855a14610468578063b5e6a0a014610485578063b65fb6cb146104a2576101ce565b80639df1b346146103e7578063a2f9a98014610404578063a6fd0b5614610421576101ce565b806348312fa311610170578063652d34301161014a578063652d3430146103595780636fdbb3c414610376578063761275bf146103a05780638be5e97f146103bd576101ce565b806348312fa3146102f55780635a332575146103125780635dd33d991461032f576101ce565b8063171b2a05116101ac578063171b2a051461025a57806327f2744914610284578063375ec420146102a1578063429fcb0d146102cb576101ce565b8063056256a8146101d35780630f2c6355146101ff57806316cddf4e14610230575b600080fd5b8180156101df57600080fd5b506101fd600480360360208110156101f657600080fd5b50356105a4565b005b61021c6004803603602081101561021557600080fd5b50356105c6565b604080519115158252519081900360200190f35b81801561023c57600080fd5b506101fd6004803603602081101561025357600080fd5b50356105e6565b81801561026657600080fd5b506101fd6004803603602081101561027d57600080fd5b50356105ed565b61021c6004803603602081101561029a57600080fd5b50356105f4565b8180156102ad57600080fd5b506101fd600480360360208110156102c457600080fd5b50356105fd565b8180156102d757600080fd5b506101fd600480360360208110156102ee57600080fd5b5035610604565b61021c6004803603602081101561030b57600080fd5b503561060b565b61021c6004803603602081101561032857600080fd5b5035610634565b81801561033b57600080fd5b506101fd6004803603602081101561035257600080fd5b5035610671565b61021c6004803603602081101561036f57600080fd5b5035610678565b81801561038257600080fd5b506101fd6004803603602081101561039957600080fd5b5035610680565b61021c600480360360208110156103b657600080fd5b5035610687565b8180156103c957600080fd5b506101fd600480360360208110156103e057600080fd5b5035610690565b61021c600480360360208110156103fd57600080fd5b5035610697565b61021c6004803603602081101561041a57600080fd5b50356106a0565b81801561042d57600080fd5b506101fd6004803603602081101561044457600080fd5b50356106a9565b61021c6004803603602081101561046157600080fd5b50356106b0565b61021c6004803603602081101561047e57600080fd5b50356106d4565b61021c6004803603602081101561049b57600080fd5b50356106dd565b61021c600480360360208110156104b857600080fd5b50356106e6565b8180156104cb57600080fd5b506101fd600480360360208110156104e257600080fd5b50356106ef565b61021c600480360360208110156104ff57600080fd5b50356106f6565b61021c6004803603602081101561051c57600080fd5b50356106ff565b61021c6004803603602081101561053957600080fd5b5035610708565b61021c6004803603602081101561055657600080fd5b503561072b565b81801561056957600080fd5b506101fd6004803603602081101561058057600080fd5b5035610734565b61021c6004803603602081101561059d57600080fd5b503561073b565b600b5b81600401601c6101000a81548160ff021916908360ff16021790555050565b600060045b6004830154600160e01b900460ff9081169116149050919050565b60016105a7565b60086105a7565b600060026105cb565b60046105a7565b60056105a7565b600481015460009060ff600160e01b909104166001148061062e575060026105cb565b92915050565b600481015460009060ff600160e01b90910416600b14806106645750600482015460ff600160e01b909104166007145b8061062e575060036105cb565b600a6105a7565b6000806105cb565b60036105a7565b600060086105cb565b60026105a7565b6000600b6105cb565b600060096105cb565b60066105a7565b6000600480830154600160e01b900460ff9081169116148061062e575060086105cb565b600060076105cb565b600060016105cb565b600060036105cb565b60096105a7565b600060066105cb565b6000600a6105cb565b600481015460009060ff600160e01b909104166005148061062e575060066105cb565b600060056105cb565b60076105a7565b600481015460009060ff600160e01b90910416600a148061062e575060096105cb56fea265627a7a723158203c165ce1b780ff4dbc007f949470084d045873490e73fbaf12e46f30def0567b64736f6c63430005110032"
abi = [{'inputs': [{'internalType': 'address',
    'name': '_masterBondedECDSAKeepAddress',
    'type': 'address'},
   {'internalType': 'address',
    'name': '_sortitionPoolFactory',
    'type': 'address'},
   {'internalType': 'address', 'name': '_tokenStaking', 'type': 'address'},
   {'internalType': 'address', 'name': '_keepBonding', 'type': 'address'},
   {'internalType': 'address', 'name': '_randomBeacon', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'constructor'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'keepAddress',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address[]',
    'name': 'members',
    'type': 'address[]'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'owner',
    'type': 'address'},
   {'indexed': True,
    'internalType': 'address',
    'name': 'application',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'uint256',
    'name': 'honestThreshold',
    'type': 'uint256'}],
  'name': 'BondedECDSAKeepCreated',
  'type': 'event'},
 {'anonymous': False,
  'inputs': [{'indexed': True,
    'internalType': 'address',
    'name': 'application',
    'type': 'address'},
   {'indexed': False,
    'internalType': 'address',
    'name': 'sortitionPool',
    'type': 'address'}],
  'name': 'SortitionPoolCreated',
  'type': 'event'},
 {'payable': True, 'stateMutability': 'payable', 'type': 'fallback'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': '_relayEntry',
    'type': 'uint256'}],
  'name': '__beaconCallback',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_delegatedAuthorityRecipient',
    'type': 'address'}],
  'name': '__isRecognized',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'balanceOf',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'callbackGas',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_application',
    'type': 'address'}],
  'name': 'createSortitionPool',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}],
  'name': 'getKeepAtIndex',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'getKeepCount',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address', 'name': '_keep', 'type': 'address'}],
  'name': 'getKeepOpenedTimestamp',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_application',
    'type': 'address'}],
  'name': 'getSortitionPool',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_application',
    'type': 'address'}],
  'name': 'getSortitionPoolWeight',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'groupSelectionSeed',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'hasMinimumStake',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'}],
  'name': 'isOperatorAuthorized',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_application', 'type': 'address'}],
  'name': 'isOperatorEligible',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_application', 'type': 'address'}],
  'name': 'isOperatorRegistered',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_application', 'type': 'address'}],
  'name': 'isOperatorUpToDate',
  'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'name': 'keeps',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'masterKeepAddress',
  'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'minimumBond',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'newEntryFeeEstimate',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'newGroupSelectionSeedFee',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': '_groupSize',
    'type': 'uint256'},
   {'internalType': 'uint256', 'name': '_honestThreshold', 'type': 'uint256'},
   {'internalType': 'address', 'name': '_owner', 'type': 'address'},
   {'internalType': 'uint256', 'name': '_bond', 'type': 'uint256'},
   {'internalType': 'uint256',
    'name': '_stakeLockDuration',
    'type': 'uint256'}],
  'name': 'openKeep',
  'outputs': [{'internalType': 'address',
    'name': 'keepAddress',
    'type': 'address'}],
  'payable': True,
  'stateMutability': 'payable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'openKeepFeeEstimate',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'poolStakeWeightDivisor',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_application',
    'type': 'address'}],
  'name': 'registerMemberCandidate',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [],
  'name': 'requestNewGroupSelectionSeed',
  'outputs': [],
  'payable': True,
  'stateMutability': 'payable',
  'type': 'function'},
 {'constant': True,
  'inputs': [],
  'name': 'reseedPool',
  'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
  'payable': False,
  'stateMutability': 'view',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'uint256',
    'name': '_minimumBondableValue',
    'type': 'uint256'},
   {'internalType': 'uint256', 'name': '_groupSize', 'type': 'uint256'},
   {'internalType': 'uint256', 'name': '_honestThreshold', 'type': 'uint256'}],
  'name': 'setMinimumBondableValue',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'},
 {'constant': False,
  'inputs': [{'internalType': 'address',
    'name': '_operator',
    'type': 'address'},
   {'internalType': 'address', 'name': '_application', 'type': 'address'}],
  'name': 'updateOperatorStatus',
  'outputs': [],
  'payable': False,
  'stateMutability': 'nonpayable',
  'type': 'function'}]
#refering to the deploy coontract
BondedECDSAKeepFactory = web3.eth.contract(address = address, abi=abi)

# TokenGrant
rrr = BondedECDSAKeepFactory.functions.getSortitionPool(web3.toChecksumAddress('0xc3f96306eDabACEa249D2D22Ec65697f38c6Da69')).call()


file = st.file_uploader(label="Import (mew) json file (-UTC-)")
# file_buffer = st.file_uploader(...)
# file = io.TextIOWrapper(file_buffer)
#st.write(file)
if file:
    file_2 = json.load(file)
    #st.write(file_2)
    json_string = json.dumps(file_2)
    lll = str(file_2)
    # st.write(json_string)
    # st.write(type(lll))
    # file_1 = file_2.read()
    dictList = []
    for key, value in file_2.items():
        #print(value)
        dictList.append(value)
    wallet_address  = dictList[2]
    # st.write(dictList)
    wallet_address_full = web3.toChecksumAddress(str('0x') + wallet_address )

    balance = web3.eth.getBalance(wallet_address_full)
    balance_eth = web3.fromWei(balance, 'ether')
    st.success(wallet_address_full)
    st.success(str('ETH value: ') + str(balance_eth))
    if balance_eth < 0.1:
        st.error('Please add ETH')


    # st.write(lll)
if file and balance_eth > 0.1:
    pass_eth = st.text_input('Enter password(Wallet JSON)', type="password")
    p = []
    if file and pass_eth:
        from web3.auto import w3
        import web3
        from web3 import Web3
        try:
            private_key = w3.eth.account.decrypt(file_2,
                                                 pass_eth)
        except:

            st.error('Try again please check pass for wallet')
        else:
            web3 = Web3(Web3.HTTPProvider(ropsten_url))


            extra_data = str(wallet_address) + str(wallet_address) + str(wallet_address)

            url = 'https://us-central1-keep-test-f3e0.cloudfunctions.net/keep-faucet-ropsten?account=%s' % wallet_address_full
            # response.text
            grant = TokenGrant.functions.getGrants(web3.toChecksumAddress(wallet_address_full)).call()
            if not grant:
                # st.error('OOOPS!Rerun page or try to get a grant or https://us-central1-keep-test-f3e0.cloudfunctions.net/keep-faucet-ropsten?account=%s' % wallet_address_full)
                # response = requests.post(url=url)
                time.sleep(10)

                grant = TokenGrant.functions.getGrants(web3.toChecksumAddress(wallet_address_full)).call()

                with st.spinner('Please wait Grant'):
                    response = requests.post(url=url)
                    sleep(20)
                    href = str(response.content)[196:262]
                    receipt = web3.eth.waitForTransactionReceipt(href)
                    grant = TokenGrant.functions.getGrants(web3.toChecksumAddress(wallet_address_full)).call()
                    for i in grant:
                        grand_id = i


                st.success('Grand № %d recieved' % grand_id)

                # for i in grant:
                #     grand_id = i
                # st.success('Grand № %d recieved' %grand_id)
            else:
                try:
                    grant = TokenGrant.functions.getGrants(web3.toChecksumAddress(wallet_address_full)).call()
                    for i in grant:
                        grand_id = i
                        st.success('Grand № %d recieved' % grand_id)

                except:
                    st.error('OOPS! Check faucet')

            signed = []
            # TokenGrant
            nonce = web3.eth.getTransactionCount(wallet_address_full)
            private_key = private_key
            extra_data = str(wallet_address) + str(wallet_address) + str(wallet_address)
            grant = TokenGrant.functions.getGrants(web3.toChecksumAddress(wallet_address_full)).call()

            GRANT_ID = grand_id
            STAKING_AMOUNT = TokenGrant.functions.balanceOf(wallet_address_full).call()
            GAS_PRICE = '5'
            txn = TokenGrant.functions.stake(GRANT_ID, '0x234d2182B29c6a64ce3ab6940037b5C8FdAB608e', STAKING_AMOUNT,
                                             extra_data).buildTransaction({
                'chainId': 3,
                'gas': 2000000,
                'gasPrice': web3.toWei(GAS_PRICE, 'gwei'),
                'value': 0,
                'nonce': nonce,
            })

            stake = TokenGrant.functions.stakeBalanceOf(web3.toChecksumAddress(wallet_address_full)).call()
            if stake != 0 and stake > 80000:
                st.success('KEEP Tokens already delegated')
                stat_1 = 1
            else:
                # st.write(STAKING_AMOUNT)

                signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
                signed.append(signed_txn)
                # signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

                tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                print(tx_hash)

                with st.spinner('Please wait delegation'):
                    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
                    stat_1 = receipt['status']
                    # st.write(receipt['status'])
                    link = str('https://ropsten.etherscan.io/tx/' + str(receipt['transactionHash'].hex()))
                st.success('KEEP Tokens delegated')
                href = f'<a href="{link}" add target="_blank" >\
                                                  >>>Check txn on Explorer<<<\
                                      </a>'

                # st.write(receipt['status'])

            minstake = KeepRandomBeaconOperator.functions.hasMinimumStake(
                web3.toChecksumAddress(wallet_address_full)).call()

            if minstake == True:
                st.success('Keep Random Beacon Operator already Contract Authorized successful')
                # st.markdown(href, unsafe_allow_html=True)
                stat_2 = 1
                # st.success(st.markdown(href, unsafe_allow_html=True))
            else:
                nonce = web3.eth.getTransactionCount(wallet_address_full)
                # TokenStaking.functions.authorizeOperatorContract(address, address)
                txn = TokenStaking.functions.authorizeOperatorContract(wallet_address_full,
                                                                       KeepRandomBeaconOperator.address).buildTransaction(
                    {
                        'chainId': 3,
                        'gas': 2000000,
                        'gasPrice': web3.toWei(GAS_PRICE, 'gwei'),
                        'value': 0,
                        'nonce': nonce,
                    })
                signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

                tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

                with st.spinner('Please wait authorization Keep Random Beacon Operator'):
                    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
                    stat_2 = receipt['status']
                    # st.write(receipt['status'])
                    link = str('https://ropsten.etherscan.io/tx/' + str(receipt['transactionHash'].hex()))
                st.success('Keep Random Beacon Operator Contract Authorized successful')
                href = f'<a href="{link}" add target="_blank">\
                                                    >>>Check txn on Explorer<<<\
                                        </a>'
                st.markdown(href, unsafe_allow_html=True)
                # st.write(receipt['status'])

            KeepFactory = BondedECDSAKeepFactory.functions.isOperatorAuthorized(wallet_address_full).call()
            if KeepFactory == False:
                nonce = web3.eth.getTransactionCount(wallet_address_full)
                TokenStaking.functions.authorizeOperatorContract(address, address)
                txn = TokenStaking.functions.authorizeOperatorContract(wallet_address_full,
                                                                       BondedECDSAKeepFactory.address).buildTransaction(
                    {
                        'chainId': 3,
                        'gas': 2000000,
                        'gasPrice': web3.toWei(GAS_PRICE, 'gwei'),
                        'value': 0,
                        'nonce': nonce,
                    })
                signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

                tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                # print(tx_hash)
                with st.spinner('Please wait authorization ECDSAKeepFactory'):
                    receipt_3 = web3.eth.waitForTransactionReceipt(tx_hash)
                    # st.write(receipt['status'])
                    stat_3 = receipt_3['status']
                    link = str('https://ropsten.etherscan.io/tx/' + str(receipt_3['transactionHash'].hex()))
                st.success('Authorize ECDSAKeepFactory confirm')
                href = f'<a href="{link}" add target="_blank">\
                                                        >>>Check txn on Explorer<<<\
                                            </a>'
                st.markdown(href, unsafe_allow_html=True)
                sleep(2)
                nonce = web3.eth.getTransactionCount(wallet_address_full)
                txn = KeepBonding.functions.authorizeSortitionPoolContract(wallet_address_full, rrr).buildTransaction({
                    'chainId': 3,
                    'gas': 2000000,
                    'gasPrice': web3.toWei(GAS_PRICE, 'gwei'),
                    'value': 0,
                    'nonce': nonce,
                })

                signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

                tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                with st.spinner('Please wait authorization TBTCSystem'):
                    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
                    # st.write(receipt['status'])
                    link = str('https://ropsten.etherscan.io/tx/' + str(receipt['transactionHash'].hex()))
                st.success('Authorize TBTCSystem confirm')
                href = f'<a href="{link}" add target="_blank">\
                                                        >>>Check txn on Explorer<<<\
                                            </a>'
                st.markdown(href, unsafe_allow_html=True)
            # st.write(receipt['status'])

            else:
                st.success('Authorize ECDSAKeepFactory confirm')
                st.success('Authorize TBTCSystem already confirm')
                stat_3 = 1

            if stat_1 >= 1 and stat_2 >= 1 and stat_3 >= 1:
                choose = st.multiselect('Choose ECDSA/BEACON', ('ecdsa', 'beacon'))

                amount_un = KeepBonding.functions.unbondedValue(wallet_address_full).call()
                balance_eth_un = web3.fromWei(amount_un, 'ether')
                st.success(balance_eth_un)
                count_eth = st.number_input('Please enter amount ETH for Bonding', value=0.5, step=0.5)
                balance = web3.eth.getBalance(wallet_address_full)
                balance_eth = web3.fromWei(balance, 'ether')

                # st.write(choose)
                if not choose:
                    st.error('Please choose')
                else:
                    if len(choose) == 1:
                        for i in choose:
                            # st.write(i)
                            if i == 'ecdsa':
                                st.success("You choosed ECDSA")

                            if i == 'beacon':
                                st.success("You choosed BEACON")
                    if len(choose) == 2:
                        st.success("You choosed ECDSA and BEACON")



                if count_eth != 0 and count_eth > 0.05 or count_eth != 0:
                    if st.button('Add ETH for bonding'):
                        if count_eth <= float(balance_eth) - 0.05:
                            amount = a = int(count_eth * 1000000000000000000)
                            nonce = web3.eth.getTransactionCount(wallet_address_full)
                            txn = KeepBonding.functions.deposit(wallet_address_full).buildTransaction({
                                'chainId': 3,
                                'gas': 2000000,
                                'gasPrice': web3.toWei(GAS_PRICE, 'gwei'),
                                'value': amount,
                                'nonce': nonce,
                            })
                            print(txn)
                            signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

                            tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                            with st.spinner('Please wait add ETH '):
                                receipt = web3.eth.waitForTransactionReceipt(tx_hash)
                                # st.write(receipt['status'])
                                stat_4 = receipt['status']
                                link = str('https://ropsten.etherscan.io/tx/' + str(receipt['transactionHash'].hex()))
                            st.success('%s ETH successful  added' % count_eth)
                            href = f'<a href="{link}" add target="_blank">\
                                                                    >>>Check txn on Explorer<<<\
                                                        </a>'
                            st.markdown(href, unsafe_allow_html=True)
                            if len(choose)==1:
                                for i in choose:
                                    # st.write(i)
                                    if i == 'ecdsa':
                                        #st.success("You choosed ESDCA")
                                        h = '-h'
                                        commands = [
                                            "sudo apt update",
                                            "yes | sudo apt install git -y",
                                            "sudo apt install docker.io curl -y",
                                            "sudo systemctl start docker",
                                            "sudo systemctl enable docker",
                                            "sudo ufw allow 22 && sudo ufw allow 3919 && sudo ufw allow 3920 && sudo ufw allow 8501 && yes | sudo ufw enable",
                                            "sudo ufw status",

                                            "git clone https://github.com/icohigh/keep-nodes.git",
                                            "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt" % wallet_address_full,
                                            "echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt" % pass_eth,
                                            "echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json" % json_string,
                                            "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
                                            "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
                                            "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
                                            "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
                                            "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                            "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                            "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                            "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                            "export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)",

                                            "sudo docker run -d \
                                        --entrypoint /usr/local/bin/keep-ecdsa \
                                        --restart always \
                                        --volume $HOME/keep-nodes/data:/mnt/data \
                                        --volume $HOME/keep-nodes/ecdsa/config:/mnt/ecdsa/config \
                                        --volume $HOME/keep-nodes/ecdsa/persistence:/mnt/ecdsa/persistence \
                                        --env KEEP_ETHEREUM_PASSWORD=%s \
                                        --env LOG_LEVEL=debug \
                                        --name keep-ecdsa \
                                        -p 3920:3919 \
                                        keepnetwork/keep-ecdsa-client:v1.2.0-rc.5 --config /mnt/ecdsa/config/config.toml start" % pass_eth
                                        ]

                                        if st.button('Run ECDSA'):
                                            # st.write ('GO')

                                            with st.spinner('Wait ... please'):
                                                for command in commands:
                                                    # st.write("-" * 2,command)
                                                    output = subprocess.run(command, shell=True)

                                                # print(data)

                                            st.success(
                                                'Congratulations, the node is up and running! (please check ECDSA logs on the server itself)')
                                            st.success('Paste on server: sudo docker logs keep-ecdsa -f --since 1m')


                                            st.success('Congratulations')
                                    if i == 'beacon':
                                        #st.success("You choosed BEACON")
                                        h = '-h'
                                        commands = [
                                            "sudo apt update",
                                            "yes | sudo apt install git -y",
                                            "sudo apt install docker.io curl -y",
                                            "sudo systemctl start docker",
                                            "sudo systemctl enable docker",
                                            "sudo ufw allow 22 && sudo ufw allow 3919 && sudo ufw allow 3920 && sudo ufw allow 8501 && yes | sudo ufw enable",
                                            "sudo ufw status",

                                            "git clone https://github.com/icohigh/keep-nodes.git",
                                            "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt" % wallet_address_full,
                                            "echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt" % pass_eth,
                                            "echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json" % json_string,
                                            "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
                                            "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
                                            "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
                                            "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
                                            "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                            "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                            "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                            "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                            "export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)",
                                            "sudo docker run -d \
                                        --entrypoint /usr/local/bin/keep-client \
                                        --restart always \
                                        --volume $HOME/keep-nodes/data:/mnt/data \
                                        --volume $HOME/keep-nodes/beacon/config:/mnt/beacon/config \
                                        --volume $HOME/keep-nodes/beacon/persistence:/mnt/beacon/persistence \
                                        --env KEEP_ETHEREUM_PASSWORD=%s \
                                        --env LOG_LEVEL=debug \
                                        --name keep-client \
                                        -p 3919:3919 \
                                        keepnetwork/keep-client:v1.3.0-rc.4 --config /mnt/beacon/config/config.toml start" % pass_eth

                                        ]

                                        if st.button('Run Beacon'):
                                            # st.write ('GO')

                                            with st.spinner('Wait ... please'):
                                                for command in commands:
                                                    # st.write("-" * 2,command)
                                                    output = subprocess.run(command, shell=True)

                                                # print(data)

                                            st.success(
                                                'Congratulations, the node is up and running! (please check BEACON logs on the server itself)')
                                            st.success('Paste on server: sudo docker logs keep-client -f --since 1m')

                                            st.success('Congratulations')

                            if len(choose) == 2:
                                #st.success("You choosed ESDCA and BEACON")
                                h = '-h'
                                commands = [
                                    "sudo apt update",
                                    "yes | sudo apt install git -y",
                                    "sudo apt install docker.io curl -y",
                                    "sudo systemctl start docker",
                                    "sudo systemctl enable docker",
                                    "sudo ufw allow 22 && sudo ufw allow 3919 && sudo ufw allow 3920 && sudo ufw allow 8501 && yes | sudo ufw enable",
                                    "sudo ufw status",

                                    "git clone https://github.com/icohigh/keep-nodes.git",
                                    "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt" % wallet_address_full,
                                    "echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt" % pass_eth,
                                    "echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json" % json_string,
                                    "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
                                    "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
                                    "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
                                    "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
                                    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                    "export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)",
                                    "sudo docker run -d \
                                --entrypoint /usr/local/bin/keep-client \
                                --restart always \
                                --volume $HOME/keep-nodes/data:/mnt/data \
                                --volume $HOME/keep-nodes/beacon/config:/mnt/beacon/config \
                                --volume $HOME/keep-nodes/beacon/persistence:/mnt/beacon/persistence \
                                --env KEEP_ETHEREUM_PASSWORD=%s \
                                --env LOG_LEVEL=debug \
                                --name keep-client \
                                -p 3919:3919 \
                                keepnetwork/keep-client:v1.3.0-rc.4 --config /mnt/beacon/config/config.toml start" % pass_eth,
                                    "sudo docker run -d \
                                --entrypoint /usr/local/bin/keep-ecdsa \
                                --restart always \
                                --volume $HOME/keep-nodes/data:/mnt/data \
                                --volume $HOME/keep-nodes/ecdsa/config:/mnt/ecdsa/config \
                                --volume $HOME/keep-nodes/ecdsa/persistence:/mnt/ecdsa/persistence \
                                --env KEEP_ETHEREUM_PASSWORD=%s \
                                --env LOG_LEVEL=debug \
                                --name keep-ecdsa \
                                -p 3920:3919 \
                                keepnetwork/keep-ecdsa-client:v1.2.0-rc.5 --config /mnt/ecdsa/config/config.toml start" % pass_eth
                                ]

                                if st.button('Run ECDSA and BEACON'):
                                    # st.write ('GO')

                                    with st.spinner('Wait ... please'):
                                        for command in commands:
                                            # st.write("-" * 2,command)
                                            output = subprocess.run(command, shell=True)

                                        # print(data)

                                    st.success(
                                        'Congratulations, the node is up and running! (please check ECDSA/BEACON logs on the server itself)')

                                    st.success('Paste on server: sudo docker logs keep-client -f --since 1m')
                                    st.success('Paste on server: sudo docker logs keep-ecdsa -f --since 1m')

                                    st.success('Congratulations')






                    if balance_eth_un > 0.05 and len(choose)==1:
                        for i in choose:
                            # st.write(i)
                            if i == 'ecdsa':
                                #st.success("You choosed ECDSA")
                                h = '-h'
                                commands = [
                                    "sudo apt update",
                                    "yes | sudo apt install git -y",
                                    "sudo apt install docker.io curl -y",
                                    "sudo systemctl start docker",
                                    "sudo systemctl enable docker",
                                    "sudo ufw allow 22 && sudo ufw allow 3919 && sudo ufw allow 3920 && sudo ufw allow 8501 && yes | sudo ufw enable",
                                    "sudo ufw status",

                                    "git clone https://github.com/icohigh/keep-nodes.git",
                                    "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt" % wallet_address_full,
                                    "echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt" % pass_eth,
                                    "echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json" % json_string,
                                    "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
                                    "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
                                    "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
                                    "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
                                    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                    "export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)",

                                    "sudo docker run -d \
                                --entrypoint /usr/local/bin/keep-ecdsa \
                                --restart always \
                                --volume $HOME/keep-nodes/data:/mnt/data \
                                --volume $HOME/keep-nodes/ecdsa/config:/mnt/ecdsa/config \
                                --volume $HOME/keep-nodes/ecdsa/persistence:/mnt/ecdsa/persistence \
                                --env KEEP_ETHEREUM_PASSWORD=%s \
                                --env LOG_LEVEL=debug \
                                --name keep-ecdsa \
                                -p 3920:3919 \
                                keepnetwork/keep-ecdsa-client:v1.2.0-rc.5 --config /mnt/ecdsa/config/config.toml start" % pass_eth
                                ]

                                if st.button('Run ECDSA without adding more ETH'):
                                    # st.write ('GO')

                                    with st.spinner('Wait ... please'):
                                        for command in commands:
                                            # st.write("-" * 2,command)
                                            output = subprocess.run(command, shell=True)

                                        # print(data)

                                    st.success(
                                        'Congratulations, the node is up and running! (please check ECDSA logs on the server itself)')
                                    st.success('Paste on server: sudo docker logs keep-ecdsa -f --since 1m')

                                    st.success('Congratulations')
                            if i == 'beacon':
                                #st.success("You choosed BEACON")
                                h = '-h'
                                commands = [
                                    "sudo apt update",
                                    "yes | sudo apt install git -y",
                                    "sudo apt install docker.io curl -y",
                                    "sudo systemctl start docker",
                                    "sudo systemctl enable docker",
                                    "sudo ufw allow 22 && sudo ufw allow 3919 && sudo ufw allow 3920 && sudo ufw allow 8501 && yes | sudo ufw enable",
                                    "sudo ufw status",

                                    "git clone https://github.com/icohigh/keep-nodes.git",
                                    "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt" % wallet_address_full,
                                    "echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt" % pass_eth,
                                    "echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json" % json_string,
                                    "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
                                    "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
                                    "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
                                    "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
                                    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                    "export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)",
                                    "sudo docker run -d \
                                --entrypoint /usr/local/bin/keep-client \
                                --restart always \
                                --volume $HOME/keep-nodes/data:/mnt/data \
                                --volume $HOME/keep-nodes/beacon/config:/mnt/beacon/config \
                                --volume $HOME/keep-nodes/beacon/persistence:/mnt/beacon/persistence \
                                --env KEEP_ETHEREUM_PASSWORD=%s \
                                --env LOG_LEVEL=debug \
                                --name keep-client \
                                -p 3919:3919 \
                                keepnetwork/keep-client:v1.3.0-rc.4 --config /mnt/beacon/config/config.toml start" % pass_eth

                                ]

                            if st.button('Run Beacon without adding more ETH'):
                                # st.write ('GO')

                                with st.spinner('Wait ... please'):
                                    for command in commands:
                                        # st.write("-" * 2,command)
                                        output = subprocess.run(command, shell=True)

                                    # print(data)

                                st.success(
                                    'Congratulations, the node is up and running! (please check ECDSA logs on the server itself)')
                                st.success('Paste on server: sudo docker logs keep-client -f --since 1m')

                                st.success('Congratulations')

                if balance_eth_un > 0.05 and len(choose) == 2:
                    #st.success("You choosed ECDSA and BEACON without adding more ETH")
                    h = '-h'
                    commands = [
                        "sudo apt update",
                        "yes | sudo apt install git -y",
                        "sudo apt install docker.io curl -y",
                        "sudo systemctl start docker",
                        "sudo systemctl enable docker",
                        "sudo ufw allow 22 && sudo ufw allow 3919 && sudo ufw allow 3920 && sudo ufw allow 8501 && yes | sudo ufw enable",
                        "sudo ufw status",

                        "git clone https://github.com/icohigh/keep-nodes.git",
                        "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt" % wallet_address_full,
                        "echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt" % pass_eth,
                        "echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json" % json_string,
                        "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
                        "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
                        "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
                        "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
                        "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                        "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                        "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                        "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                        "export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)",
                        "sudo docker run -d \
                    --entrypoint /usr/local/bin/keep-client \
                    --restart always \
                    --volume $HOME/keep-nodes/data:/mnt/data \
                    --volume $HOME/keep-nodes/beacon/config:/mnt/beacon/config \
                    --volume $HOME/keep-nodes/beacon/persistence:/mnt/beacon/persistence \
                    --env KEEP_ETHEREUM_PASSWORD=%s \
                    --env LOG_LEVEL=debug \
                    --name keep-client \
                    -p 3919:3919 \
                    keepnetwork/keep-client:v1.3.0-rc.4 --config /mnt/beacon/config/config.toml start" % pass_eth,
                        "sudo docker run -d \
                    --entrypoint /usr/local/bin/keep-ecdsa \
                    --restart always \
                    --volume $HOME/keep-nodes/data:/mnt/data \
                    --volume $HOME/keep-nodes/ecdsa/config:/mnt/ecdsa/config \
                    --volume $HOME/keep-nodes/ecdsa/persistence:/mnt/ecdsa/persistence \
                    --env KEEP_ETHEREUM_PASSWORD=%s \
                    --env LOG_LEVEL=debug \
                    --name keep-ecdsa \
                    -p 3920:3919 \
                    keepnetwork/keep-ecdsa-client:v1.2.0-rc.5 --config /mnt/ecdsa/config/config.toml start" % pass_eth
                    ]

                    if st.button('Run ECDSA and BEACON without adding more ETH'):
                        # st.write ('GO')

                        with st.spinner('Wait ... please'):
                            for command in commands:
                                # st.write("-" * 2,command)
                                output = subprocess.run(command, shell=True)

                            # print(data)

                        st.success(
                            'Congratulations, the node is up and running! (please check ECDSA logs on the server itself)')
                        st.success('Paste on server: sudo docker logs keep-client -f --since 1m')
                        st.success('Paste on server: sudo docker logs keep-ecdsa -f --since 1m')

                        st.success('Congratulations')





