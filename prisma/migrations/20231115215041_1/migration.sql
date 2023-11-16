-- CreateTable
CREATE TABLE "Token" (
    "id" TEXT NOT NULL,
    "unique_hash" TEXT NOT NULL,
    "tx_hash" TEXT NOT NULL,
    "media_url" TEXT NOT NULL,
    "owner" TEXT NOT NULL,

    CONSTRAINT "Token_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Token_unique_hash_key" ON "Token"("unique_hash");

-- CreateIndex
CREATE UNIQUE INDEX "Token_tx_hash_key" ON "Token"("tx_hash");
