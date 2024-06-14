def calc_bearing(latitude1, longitude1, latitude2, longitude2):
    """
    Calculates the bearing between two coordinates.

    Parameters
    ----------
    lat1 & lon1 : latitude and longitude of point 1 in degrees
    lat2 & lon2 : latitude and longitude of point 1 in degrees

    Return
    -------
    The resulting angle is the bearing from the first coordinate to the 
    second coordinate, measured in degrees clockwise from north.
    
    Reference:
    ----------
    - https://mapscaping.com/how-to-calculate-bearing-between-two-coordinates/
    - https://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/
    - https://www.sunearthtools.com/tools/distance.php (used this calc. tool to verify)
    """
    from math import atan2, cos, sin, degrees, radians
    
    # Convert latitude and lonitude to radians
    lat1 = radians(latitude1)
    lon1 = radians(longitude1)
    lat2 = radians(latitude2)
    lon2 = radians(longitude2)
    
    # Calculate the bearing
    x = sin(lon2 - lon1) * cos(lat2)
    y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(lon2 - lon1)
    bearing = atan2(x, y)
    
    # Convert the bearing to degrees
    bearing = degrees(bearing)
    
    # Make sure the bearing is positive
    bearing = (bearing + 360) % 360
    
    return bearing


def geodetic_to_Cartesian(latitude, longitude, height):
    
    """
    Return geocentric (Cartesian) Coordinates x, y, z corresponding to
    the geodetic coordinates given by latitude and longitude (in
    degrees) and height above ellipsoid. The ellipsoid is
    specified by a pair (semi-major axis, reciprocal flattening) 
    accoriding to WGS84.
    
    Return
    -------
    x,y,z cartesian coordinates in meter
    
    Reference:
    ----------
    - http://walter.bislins.ch/bloge/index.asp?page=Globe+and+Flat+Earth+Transformations+and+Mappings
    - https://en.wikipedia.org/wiki/Geographic_coordinate_conversion
    """
    
    from math import cos, radians, sin, sqrt
    
    ellipsoid = 6378137, 298.257223563 # (semi-major axis, reciprocal flattening) accoriding to WGS84
    φ = radians(latitude)
    λ = radians(longitude)
    sin_φ = sin(φ)
    a, rf = ellipsoid           # semi-major axis, reciprocal flattening
    e2 = 1 - (1 - 1 / rf) ** 2  # eccentricity squared
    n = a / sqrt(1 - e2 * sin_φ ** 2) # prime vertical radius
    r = (n + height) * cos(φ)   # perpendicular distance from z axis
    x = r * cos(λ)
    y = r * sin(λ)
    z = (n * (1 - e2) + height) * sin_φ
    return x, y, z
    
    