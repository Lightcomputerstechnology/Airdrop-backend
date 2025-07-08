// database/airdrops_model.js

export const AirdropModel = {
  title: String,
  description: String,
  blockchain: String,
  reward: String,
  claimLink: String,
  tasks: [
    {
      type: String, // e.g., "twitter", "telegram", "wallet_connect"
      detail: String,
      actionURL: String,
    },
  ],
  status: {
    type: String, // "new", "claimed", "expired"
    default: "new",
  },
  expiresAt: Date,
  createdAt: {
    type: Date,
    default: () => new Date(),
  },
};
