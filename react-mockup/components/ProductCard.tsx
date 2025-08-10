import { useState } from 'react';
import { ShoppingCart, Heart, Eye } from 'lucide-react';
import { motion } from 'framer-motion';

interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  discount?: number;
  image: string;
  category: string;
}

interface ProductCardProps {
  product: Product;
  onAddToCart: (productId: number) => void;
  onToggleWishlist: (productId: number) => void;
  isInWishlist: boolean;
}

export const ProductCard: React.FC<ProductCardProps> = ({
  product,
  onAddToCart,
  onToggleWishlist,
  isInWishlist
}) => {
  const [isHovered, setIsHovered] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const discountedPrice = product.discount 
    ? product.price * (1 - product.discount / 100)
    : product.price;

  const handleAddToCart = async () => {
    setIsLoading(true);
    await onAddToCart(product.id);
    setIsLoading(false);
  };

  return (
    <motion.div
      className="group relative bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-2xl transition-all duration-300"
      whileHover={{ y: -8 }}
      onHoverStart={() => setIsHovered(true)}
      onHoverEnd={() => setIsHovered(false)}
    >
      {/* Discount Badge */}
      {product.discount && (
        <div className="absolute top-4 right-4 z-10 bg-red-500 text-white px-3 py-1 rounded-full text-sm font-semibold">
          -{product.discount}%
        </div>
      )}

      {/* Image Container */}
      <div className="relative overflow-hidden">
        <img
          src={product.image}
          alt={product.name}
          className="w-full h-64 object-cover transition-transform duration-300 group-hover:scale-110"
        />
        
        {/* Overlay Actions */}
        <motion.div
          className="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center space-x-4"
          initial={{ opacity: 0 }}
          animate={{ opacity: isHovered ? 1 : 0 }}
          transition={{ duration: 0.2 }}
        >
          <motion.button
            className="bg-white text-gray-800 p-3 rounded-full hover:bg-gray-100 transition-colors"
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.95 }}
          >
            <Eye size={20} />
          </motion.button>
          
          <motion.button
            className={`p-3 rounded-full transition-colors ${
              isInWishlist 
                ? 'bg-red-500 text-white' 
                : 'bg-white text-gray-800 hover:bg-gray-100'
            }`}
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => onToggleWishlist(product.id)}
          >
            <Heart size={20} fill={isInWishlist ? 'currentColor' : 'none'} />
          </motion.button>
        </motion.div>
      </div>

      {/* Content */}
      <div className="p-6">
        <h3 className="font-semibold text-lg text-gray-800 mb-2 line-clamp-2">
          {product.name}
        </h3>
        
        <p className="text-gray-600 text-sm mb-4 line-clamp-2">
          {product.description}
        </p>

        {/* Price Section */}
        <div className="flex items-center justify-between mb-4">
          <div className="flex flex-col">
            {product.discount ? (
              <>
                <span className="text-lg font-bold text-green-600">
                  ${discountedPrice.toFixed(2)}
                </span>
                <span className="text-sm text-gray-500 line-through">
                  ${product.price.toFixed(2)}
                </span>
              </>
            ) : (
              <span className="text-lg font-bold text-gray-800">
                ${product.price.toFixed(2)}
              </span>
            )}
          </div>
          
          <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
            ID: {product.id}
          </span>
        </div>

        {/* Add to Cart Button */}
        <motion.button
          className="w-full bg-gray-900 text-white py-3 px-4 rounded-lg font-semibold flex items-center justify-center space-x-2 hover:bg-gray-800 transition-colors disabled:opacity-50"
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={handleAddToCart}
          disabled={isLoading}
        >
          <ShoppingCart size={20} />
          <span>{isLoading ? 'Adding...' : 'Add to Cart'}</span>
        </motion.button>
      </div>
    </motion.div>
  );
};