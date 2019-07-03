pragma solidity >=0.4.22 <0.6.0;
contract Agri {

    mapping(string => bytes32) farmPicHash;


    function addNewHash(string memory id ,bytes32 picHash) public {
        farmPicHash[id] = picHash;
    }

    function getPicHash(string memory id) public view returns(bytes32) {
        return farmPicHash[id] ;
    }

}