plink2 \
  --vcf Genetic-Variation/project/testdata/vcf/chr22_test.vcf \
  --make-bed \
  --snps-only \
  --maf 0.08 \
  --geno 0.02 \
  --mind 0.2 \
  --recode \
  --out chr22

