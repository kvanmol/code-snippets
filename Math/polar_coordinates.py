def eucldistance_3Dpolar(lat1, lon1, r1, lat2, lon2, r2):
    """
    Calculates the euclidean distance 'd' between 2 points given 
    spherical polar coordinates
    
    euclidean distance in cartesian coordinates is given by:
    d**2 = (x2−x1)**2 + (y2−y1)**2 + (z2−z1)**2
    
    if we transform x,y,z to r,θ,ϕ for each point with
    x = r*cosθ*cosϕ
    y = r*cosθ*sinϕ
    z = r*sinθ
    
    we get
    d**2 = r1**2 + r2**2 − 2*r1*r2*(cosθ1*cosθ2*cos(ϕ1−ϕ2)+ sinθ1sinθ2)
    
    note: use earth radius at the equator (6372795.477598m) for 
    calculating distance between two coordinates
    https://www.sunearthtools.com/tools/distance.php (used this calc. tool to verify)

    Parameters
    ----------
    lat1, lon1: latitude and longitude of point 1 in degrees
    r1: radius of point 1
    
    lat2, lon2: latitude and longitude of point 2 in degrees
    r2: radius of point 2

    Returns
    -------
    distance 'd' between two points, units are the same as the radii 'r1' & 'r2'
        
    Reference
    ---------
    - https://math.stackexchange.com/questions/1078231/distance-between-2-points-in-3d-space-in-spherical-polar-coordinates

    """
    from math import cos, sin, radians, degrees, sqrt
    θ1 = radians(lat1)
    ϕ1 = radians(lon1)
    θ2 = radians(lat2)
    ϕ2 = radians(lon2)
    
    return sqrt(r1**2 + r2**2 - 2*r1*r2*(cos(θ1)*cos(θ2)*cos(ϕ1 - ϕ2) + sin(θ1)*sin(θ2)))
    
    
