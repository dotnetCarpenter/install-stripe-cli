set -o pipefail

LC_ALL=C sed '/^#.*$/d' $1 | sed '/^\s*$/d' | wc -l | awk '{s+=$1} END {printf "%.0f Lines Of Code\n", s}'
