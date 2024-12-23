/*
  # Initial Schema Setup

  1. New Tables
    - `categories`
      - `id` (uuid, primary key)
      - `name` (text, not null)
      - `description` (text)
      - `created_at` (timestamp)
    
    - `products`
      - `id` (uuid, primary key)
      - `category_id` (uuid, foreign key)
      - `name` (text, not null)
      - `price` (decimal, not null)
      - `stock` (integer, not null)
      - `created_at` (timestamp)
    
    - `orders`
      - `id` (uuid, primary key)
      - `product_id` (uuid, foreign key)
      - `quantity` (integer, not null)
      - `total_price` (decimal, not null)
      - `status` (text, not null)
      - `created_at` (timestamp)

  2. Security
    - Enable RLS on all tables
    - Add policies for authenticated users
*/

-- Categories table
CREATE TABLE categories (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  description text,
  created_at timestamptz DEFAULT now()
);

ALTER TABLE categories ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow read access to all users"
  ON categories FOR SELECT
  TO authenticated
  USING (true);

CREATE POLICY "Allow insert to authenticated users"
  ON categories FOR INSERT
  TO authenticated
  WITH CHECK (true);

CREATE POLICY "Allow update to authenticated users"
  ON categories FOR UPDATE
  TO authenticated
  USING (true);

CREATE POLICY "Allow delete to authenticated users"
  ON categories FOR DELETE
  TO authenticated
  USING (true);

-- Products table
CREATE TABLE products (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  category_id uuid REFERENCES categories(id) ON DELETE CASCADE,
  name text NOT NULL,
  price decimal(10,2) NOT NULL DEFAULT 0,
  stock integer NOT NULL DEFAULT 0,
  created_at timestamptz DEFAULT now()
);

ALTER TABLE products ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow read access to all users"
  ON products FOR SELECT
  TO authenticated
  USING (true);

CREATE POLICY "Allow insert to authenticated users"
  ON products FOR INSERT
  TO authenticated
  WITH CHECK (true);

CREATE POLICY "Allow update to authenticated users"
  ON products FOR UPDATE
  TO authenticated
  USING (true);

CREATE POLICY "Allow delete to authenticated users"
  ON products FOR DELETE
  TO authenticated
  USING (true);

-- Orders table
CREATE TABLE orders (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  product_id uuid REFERENCES products(id) ON DELETE CASCADE,
  quantity integer NOT NULL DEFAULT 1,
  total_price decimal(10,2) NOT NULL DEFAULT 0,
  status text NOT NULL DEFAULT 'pending',
  created_at timestamptz DEFAULT now()
);

ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow read access to all users"
  ON orders FOR SELECT
  TO authenticated
  USING (true);

CREATE POLICY "Allow insert to authenticated users"
  ON orders FOR INSERT
  TO authenticated
  WITH CHECK (true);

CREATE POLICY "Allow update to authenticated users"
  ON orders FOR UPDATE
  TO authenticated
  USING (true);

CREATE POLICY "Allow delete to authenticated users"
  ON orders FOR DELETE
  TO authenticated
  USING (true);