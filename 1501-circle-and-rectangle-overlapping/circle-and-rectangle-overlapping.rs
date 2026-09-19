impl Solution {
    pub fn check_overlap(
        radius: i32,
        x_center: i32,
        y_center: i32,
        x1: i32,
        y1: i32,
        x2: i32,
        y2: i32,
    ) -> bool {
        match (
            x1 <= x_center && x_center <= x2,
            y1 <= y_center && y_center <= y2,
        ) {
           
            (true, true) => return true, // 1.
            (true, false) => return (y1 - y_center).abs().min((y2 - y_center).abs()) <= radius, // 2.
            (false, true) => return (x1 - x_center).abs().min((x2 - x_center).abs()) <= radius, // 3.
            (false, false) => (),
        }

        let (x_distance, y_distance) = ( // 4.
            (x1 - x_center).abs().min((x2 - x_center).abs()),
            (y1 - y_center).abs().min((y2 - y_center).abs()),
        );
        if x_distance >= radius || y_distance >= radius { // 5.
            return false;
        }
        x_distance * x_distance + y_distance * y_distance <= radius * radius // 6.
    }
}