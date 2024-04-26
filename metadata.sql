CREATE TABLE business (
  business_id VARCHAR(50) PRIMARY KEY, -- Unique ID for each business
  name VARCHAR(255), -- Name of the business
  address VARCHAR(255), -- address of the business
  city VARCHAR(100), -- city where the business is located
  state VARCHAR(10), -- state with two letter US code where the business is located
  postal_code VARCHAR(20), -- US zip code where the business is located
  latitude DECIMAL(10,7), -- latitude coordinates of the business location
  longitude DECIMAL(10,7), -- longitude coordinates of the business location
  stars DECIMAL(2,1), -- number of star rating for the business
  review_count INTEGER,  -- total number of reviews for the business
  is_open INTEGER,  -- is the business open
  attributes JSONB, -- Json formatted attributes of the business
  categories VARCHAR(1000), -- categories that business belongs to
  hours JSONB -- business open hours in a week grouped by day
);

CREATE TABLE  (
   review_id VARCHAR(50) PRIMARY KEY, -- Unique ID for each review
   user_id VARCHAR(50), -- user ID of the user who wrote this review
   business_id VARCHAR(50) -- business ID of the business on which this review was written
   stars INTEGER, -- total stars given for this review
   useful INTEGER, -- is this review useful, 1 for useful 0 for not useful
   funny INTEGER, -- is this review funny, 1 for funny 0 for not funny
   cool integer, -- is this review cool, 1 for cool 0 for not cool
   review_text TEXT, -- review text which contains the original review given by user
   date DATE -- Date on which this review was given
);

-- business.business_id can be joined with review.business_id