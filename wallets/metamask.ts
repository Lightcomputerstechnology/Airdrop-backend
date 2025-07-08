// wallets/metamask.ts

import { ethers } from "ethers";

export async function connectMetaMask(): Promise<string | null> {
  if (!window.ethereum) return null;

  try {
    const accounts = await window.ethereum.request({
      method: "eth_requestAccounts",
    });
    return accounts[0];
  } catch (err) {
    console.error("MetaMask connection error:", err);
    return null;
  }
}

export async function withdrawToken(
  contractAddress: string,
  toAddress: string,
  amount: string
) {
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const signer = provider.getSigner();

  const erc20ABI = [
    "function transfer(address to, uint amount) public returns (bool)",
  ];

  const contract = new ethers.Contract(contractAddress, erc20ABI, signer);
  const tx = await contract.transfer(toAddress, ethers.utils.parseUnits(amount));
  return await tx.wait();
}
