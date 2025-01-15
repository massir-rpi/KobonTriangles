from poly_point_isect import isect_segments_include_segments

def count_triangle_flat_in_neg_out(points):
    return -1 * count_triangles(totuple(points.reshape(points.size // 4, 2, 2)))

def count_triangles(lines):
    isects = isect_segments_include_segments(lines)
    isects.sort(key=lambda x: x[0][0])
    lasts = dict()
    num_triangles = 0
    for i, isect in isects:
        if isect[0] in lasts and isect[1] in lasts and lasts[isect[0]] == lasts[isect[1]]:
            num_triangles += 1
        lasts[isect[0]] = isect[1]
        lasts[isect[1]] = isect[0]
    return num_triangles

def totuple(arr):
    if arr.shape == ():
        return arr.item()
    else:
        return tuple(map(totuple, arr))

if __name__ == '__main__':
    # print(count_triangles([((-1,-1),(1,1)),((1,0),(-1,2)),((0,-1),(0,2))]))
    print(count_triangles(
        [
            ((0,0),(8,0)),
            ((0,-1),(6,5)),
            ((0,7),(8,-1)),
            ((0,3),(5,-2)),
            ((3,-2),(8,3))
        ]
    ))
