def agr_cows(N, C, free_sections):
    free_sections.sort()

    def count_cows(min_distance):
        count = 1
        last_pos = free_sections[0]
        for i in range(1, N):
            if free_sections[i] - last_pos >= min_distance:
                count += 1
                last_pos = free_sections[i]
        return count
    left = 1
    right = free_sections[-1] - free_sections[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if count_cows(mid) >= C:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
