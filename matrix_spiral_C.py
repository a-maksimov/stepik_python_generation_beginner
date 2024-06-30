Denis
Tunin, [12.11.2022 18: 53]

# include <cstdlib>
# include <cstdio>
# include <cstdint>
# include <cstring>
# include <cerrno>
# include <iostream>
# include <string>
# include <vector>


class Matrix final


{

    Matrix(Matrix
const & ) = delete;
Matrix & operator = (Matrix const &) = delete;

char \
* p_format;

size_t
cntY, \
cntX;

::std::vector < uint64_t > \
       vec;

uint64_t & set(uint32_t
y, uint32_t
x )
{
return this->vec[y * cntX + x];
}

uint64_t
get(uint32_t
y, uint32_t
x ) const
{
return this->vec[y * cntX + x];
}

uint64_t
fill
    (
uint32_t
top,
uint32_t
left,
uint32_t
bottom,
uint32_t
right,
uint64_t
value
)
{
Matrix & me = *this;

uint32_t
y,
x;

do
{
if (top == bottom)
{
for (x = left; x <= right; ++x)
me.set(top, x) = ++value;
break;
}
else
{
for (x = left; x < right; ++x)
    me.set(top, x) = ++value;
}

if (left == right)
{
for (y = top; y <= bottom; ++y)
    me.set(y, right) = ++value;
break;
}
else
{
for (y = top; y < bottom; ++y)
    me.set(y, right) = ++value;
}

for (x = right; x > left; --x)
me.set(bottom, x) = ++value;

for ( y = bottom; y > top; --y )
me.set( y, left ) = ++value;

if ( (++top) > (--bottom) )
break;

if ((++left) > (--right))
    break;

value = me.fill(top, left, bottom, right, value);

} while (0);

return value;
}


void
free()
noexcept
{
Matrix & me = *this;
void * p_ = me.p_format;
if (nullptr != p_)
    {
        me.p_format = nullptr;
    ::std::free(p_);
    }
    }

    public:

    ~Matrix()
    noexcept
    {
    Matrix & me = *this;
    me.free();
    me.cntY = 0;
    me.cntX = 0;
    me.vec.clear();
    }


    Matrix()
    : p_format(nullptr)
    , cntY(0)
    , cntX(0)
    {}

    Matrix(Matrix & & src)
    : p_format(nullptr)
    , cntY(0)
    , cntX(0)
    {
    Matrix & me = *this;
    me.p_format = src.p_format;
    src.p_format = nullptr;
    me.cntY = src.cntY;
    me.cntX = src.cntX;
    me.vec =::std::move(src.vec);
    }


    Matrix & operator = (Matrix & & src)
    {
    Matrix & me = *this;
    if (& src != this)
        {
            me.free();
        me.p_format = src.p_format;
        src.p_format = nullptr;
        me.cntY = src.cntY;
        me.cntX = src.cntX;
        me.vec =::std::move(src.vec);
        }
        return me;
        }


        Matrix(uint32_t
        cntY, uint32_t
        cntX )
        : p_format(nullptr)
        , cntY(cntY)
        , cntX(cntX)
        , vec(cntY * cntX)
        {
        Matrix & me = *this;

        size_t
        constexpr
        bufsz = 256;

        do
        {
            errno = EINVAL;
        if (!cntY | | !cntX)
            break;

        uint64_t
        value = me.fill(0, 0, cntY - 1, cntX - 1, 0);

        errno = 0;
        me.p_format = (char *)::std::malloc(bufsz);
        if (nullptr == me.p_format)
            break;
        else
            ::std::memset(me.p_format, 0, bufsz);

        errno = 0;
        size_t
        cnt =::snprintf(me.p_format, bufsz, "%llu", value);
        if (!( bufsz > cnt) )
        break;
        else
        cnt =::std::strlen(me.p_format);

        errno = 0;
        cnt =::snprintf(me.p_format, bufsz, " %%#%llullu", cnt);
        if (!( bufsz > cnt) )
        break;

        return;
        } while (0);

        me.free();
        throw::std::string(::std::strerror(errno) );
        }

        void
        show()
        const
        {
        Matrix
        const & me = *this;
        ::std::printf("\n");

        if (!me.vec.empty() )
        {
            uint32_t
        x = 0;

        for (uint64_t value: me.vec)
        {
        if (!( x < cntX) )
        {
        ::
            std::printf("\n");
        x = 0;
        }

        ::std::printf(me.p_format, value);
        ++x;
        }
        }
        }

        }; // --


        class Matrix final


        int
        main(int
        argc, char ** argv )
        {
            Matrix
        matrix;

        Denis
        Tunin, [12.11.2022 18: 53]


        try
            {
                uint32_t
            rows, \
            cols;

            ::std::cin >> rows;
            ::std::cin >> cols;

            matrix = Matrix(rows, cols);
            matrix.show();
            }
            catch(::std::string
            const & x )
            {
            ::std::printf("\n%s\n", x.c_str());
            return 1;
            }

            return 0;
        }