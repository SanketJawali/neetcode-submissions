func minEatingSpeed(piles []int, h int) int {
    sort.Ints(piles)

    l, r := 1, piles[len(piles) - 1]
    k := r

    for l <= r {
        rate := int((l + r) / 2)
        var hrs int

        for _, pile := range(piles) {
            hrs += (pile + rate - 1) / rate
        }

        if hrs > h {
            l = rate + 1
        } else {
            r = rate - 1
            if rate < k {
                k = rate
            }
        }
    }

    return k
}