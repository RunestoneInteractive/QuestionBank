.. activecode:: sql_bikeshare_join_sol1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: httlads
    :chapter: PredictiveAnalytics
    :subchapter: joining_SQL
    :topics: PredictiveAnalytics/joining_SQL
    :from_source: T

    SELECT
    station_id, AVG(duration)
    FROM
    trip_data JOIN bikeshare_stations
    ON
    start_station = station_id
    WHERE
    member_type = 'Member'
    AND start_station = end_station
    AND status = 'open'
    GROUP BY
    station_id
    LIMIT
    10