SELECT x, y, z,
    IF((x+y+z) - GREATEST(x, y, z) > GREATEST(x, y, z), 'Yes', 'No') AS triangle
FROM Triangle
