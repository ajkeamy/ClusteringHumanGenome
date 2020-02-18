plink2 \
  --vcf /datasets/dsc180a-wi20-public/Genome/vcf/sample/chr22_test.vcf.gz \
  --make-bed \
  --snps-only \
  --maf 0.08 \
  --geno 0.02 \
  --mind 0.2 \
  --recode \
  --out chr22

