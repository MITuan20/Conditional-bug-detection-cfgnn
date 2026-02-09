### Spoon-based Data Processing

For AST-level and control-flow analysis, this project uses **Spoon**, following the original implementation provided by the authors.

**Environment requirements (as specified by the original implementation):**
- Apache Maven 3.3.9
- Java 1.8.0_282

**Usage:**
```bash
cd spoon/
mvn compile
mvn exec:java \
  -Dexec.mainClass="fr.inria.controlflow.Main" \
  -Dexec.args="../data/dataset.csv ../data/dataset_final.csv"
