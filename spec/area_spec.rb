require 'rspec'
require_relative 'area'

RSpec.describe Rectangle do
  describe "#area" do
    it "calculates the area of the rectangle" do
      rectangle = Rectangle.new(3, 4)
      expect(rectangle.area).to eq(12)
    end
  end

  describe "#perimeter" do
    it "calculates the perimeter of the rectangle" do
      rectangle = Rectangle.new(4, 5)
      expect(rectangle.perimeter).to eq(18)
    end
  end
end

RSpec.describe Square do
  describe "#area" do
    it "calculates the area of the square" do
      square = Square.new(7)
      expect(square.area).to eq(49)
    end
  end

  describe "#perimeter" do
    it "calculates the perimeter of the square" do
      square = Square.new(8)
      expect(square.perimeter).to eq(32)
    end
  end
end

RSpec.describe Cube do
  describe "#surface_area" do
    it "calculates the surface area of the cube" do
      cube = Cube.new(6)
      expect(cube.surface_area).to eq(216)
    end
  end

  describe "#volume" do
    it "calculates the volume of the cube" do
      cube = Cube.new(4)
      expect(cube.volume).to eq(64)
    end
  end
end
