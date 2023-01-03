import PropTypes from 'prop-types';
// @mui
import { Box, Card, Link, Typography, Stack } from '@mui/material';
import { styled } from '@mui/material/styles';
// utils
import { fCurrency } from '../../../utils/formatNumber';
// components
import Label from '../../../components/label';
import { ColorPreview } from '../../../components/color-utils';

// ----------------------------------------------------------------------

const StyledProductImg = styled('img')({
  top: 0,
  width: '100%',
  height: '100%',
  objectFit: 'cover',
  position: 'absolute',
});

// ----------------------------------------------------------------------

ShopProductCard.propTypes = {
  product: PropTypes.object,
};

export default function ShopProductCard({ product }) {
  const { atcId, category, clrNm, depPlace, fdFilePathImg, fdPrdNm, fdSbjt, fdYmd } = product;
  return (
    <Card id={atcId}>
      <Box sx={{ pt: '100%', position: 'relative' }}>
        <StyledProductImg alt={category} src={fdFilePathImg} />
      </Box>

      <Stack spacing={2} sx={{ p: 3 }}>
        <Link color="inherit" underline="hover">
          <Typography variant="h6" noWrap>
            {category}

          </Typography>
        </Link>

        <Stack direction="row" alignItems="center" justifyContent="space-between">
          {/* <ColorPreview colors={colors} /> */}
          <Typography variant="subtitle1">
            {fdYmd}
          </Typography>
          <Typography variant="subtitle1">
            &nbsp;
            {clrNm}
          </Typography>
        </Stack>
      </Stack>
    </Card>
  );
}
