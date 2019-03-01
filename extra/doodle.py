import solutions.libEuler as e


def probs_31(target):
  coins = [1, 2, 5, 10, 20, 50, 100, 200]
  ways_to_make = {c: 1 for c in range(0, target+1)}

  for c in coins[1:]:
    for k in ways_to_make:
      ref_k = k - c
      if (ref_k) in ways_to_make:
        ways_to_make[k] += ways_to_make[ref_k]
      print(c, k, ways_to_make[k])

  return ways_to_make[target], len(ways_to_make)



def find_factor(lst):
    factor = 0
    for i in range(max(lst), 0, -1):
        if all([p%i==0 for p in lst]):
            factor = i
            return factor

def e32():
    pandigits = '123456789'
    result = []

    # set up aa loop for our number A, starting with determining its order of magnitude
    # we can stop at 4, because 1111 x 1 = 1111 (which totals 9 digits)
    # Therefore, there's no base number of 5 digits that, when multiplied with a 6th digit,
    # and combined with its product wil be under 10 digits long.
    for oom_a in range(1, 5):
        # NOTE that we'll only be multiplying small a's with larger b's, so this limit could be a lot lower that OoM 4,
        # but the code below takes care of that.

        # Now for number b:
        # The answer of the multiplication should be in the order of magnitude 9 - (len(a) + len(b))
        # Multiplying two numbers will always adhere to the rule:
        #       Length of a*b is always len(a) + len(b) - (0 or 1)
        # So, knowing the order of magnitude on A and setting a proxy oom for B, we can guess if those add up:
        possible_oombs = []
        for oomb_prox in range(oom_a, 10-oom_a):
            if 2 * (oom_a + oomb_prox) - 1 <= 9:
                possible_oombs.append(oomb_prox)

        # Get all the numbers of length oom_a
        for a in range(10**(oom_a-1), 10**oom_a):
            # and B
            for oom_b in possible_oombs:
                for b in range(10**(oom_b-1), 10**oom_b):
                    # get our pandigits candidate:
                    pdc = ''.join(sorted("{}{}{}".format(a, b, a*b)))
                    if len(pdc) > 9:    # a*b result is too big, we're done here
                        break

                    if pdc != pandigits:    # a*b result is too big, we're done here
                        continue


                    result.append(a*b)
    print(result)
    return sum(result), sum(set(result))

#print(probs_31(200))
print(e32())