// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract FireAnEvent {
    uint256 controlSeed = 0;

    //Declare an Event
    event TestEvent(address indexed from, uint256 number);

    function fireEvent() public {
        controlSeed++;

        //Emit an event
        emit TestEvent(msg.sender, controlSeed);
    }
}
