from typing import Tuple

import nltk
import numpy as np

from get_drg_api.code_definitions import definitions, codes


def text_to_code(text: str) -> Tuple[str, float]:
  text = text.strip()
  print(text)
  dists = [nltk.jaccard_distance(definition, set(text.split(" "))) for definition in definitions]
  min_dist_index = np.argmin(dists)
  min_dist = dists[min_dist_index]
  code = codes[min_dist_index]
  return code, min_dist


if __name__ == '__main__':
  text = "Andere Verbrennungen mit Hauttransplantation und kompliz. Prozedur oder "  # Y02A
  code, distance = text_to_code(text)
  print(code)
  print(distance)
